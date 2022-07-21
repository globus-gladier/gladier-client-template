#!/usr/bin/env python

# Enable Gladier Logging
# import gladier.tests

import argparse
import os
import pathlib


from gladier import GladierBaseClient, generate_flow_definition

##Import individual functions
from tools.xpcs_pre_publish import PrePublish
from tools.xpcs_acquire_nodes import AcquireNodes
from tools.xpcs_boost_corr import BoostCorr
from tools.xpcs_plot import MakeCorrPlots
from tools.xpcs_gather_metadata import GatherXPCSMetadata
from tools.xpcs_publish import Publish


@generate_flow_definition(modifiers={
#    'publish_gather_metadata': {'payload': '$.GatherXpcsMetadata.details.result[0]'}
})
class XPCSBoost(GladierBaseClient):
    globus_group = '368beb47-c9c5-11e9-b455-0efb3ba9a670'
    gladier_tools = [
        "gladier_tools.globus.transfer.Transfer:FromStorage",
        BoostCorr,
        MakeCorrPlots,
    ]

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datadir", help="input file pathname", default="~/gladier_demo/xpcs/")
    parser.add_argument("--samplename", help="input file pathname", default="demo1")
    parser.add_argument('--gpu_flag', type=int, default=-1, help='''Choose which GPU to use. if the input is -1, then CPU is used''')
    return parser.parse_args()


if __name__ == '__main__':
    args = arg_parse()

    sample_name = args.samplename
    data_dir = os.path.join(args.datadir, sample_name)
    run_label = "DEMO XPCS: " + sample_name
    
    raw_name = 'A001_Aerogel_1mm_att6_Lq0_001_00001-01000.imm'
    hdf_name = 'A001_Aerogel_1mm_att6_Lq0_001_0001-1000.hdf'
    qmap_name = 'comm201901_qmap_aerogel_Lq0.h5'
    dataset_name = hdf_name[:hdf_name.rindex('.')] #remove file extension

    dataset_dir = data_dir

    # # Generate Destination Pathnames.
    raw_file = os.path.join(dataset_dir, raw_name)
    qmap_file = os.path.join(dataset_dir, qmap_name)
    #do need to transfer the metadata file because corr will look for it
    #internally even though it is not specified as an argument
    input_hdf_file = os.path.join(dataset_dir, hdf_name)
    output_hdf_file = os.path.join(dataset_dir, 'output', hdf_name)
    # Required by boost_corr to know where to stick the output HDF
    output_dir = os.path.join(dataset_dir, 'output')
    # This tells the corr state where to place version specific info
    execution_metadata_file = os.path.join(dataset_dir, 'execution_metadata.json')

    flow_input = {
        'input': {

            # processing variables
            "sample_name": sample_name,
            "data_dir": data_dir,  # relative to endpoint
            "proc_dir": data_dir,  # relative to funcx

            # REMOTE DEMO ENDPOINT FOR PTYCHO DATA
            "from_storage_transfer_source_endpoint_id": "a17d7fac-ce06-4ede-8318-ad8dc98edd69", 
            "from_storage_transfer_source_path": "/XPCS/A001_Aerogel_1mm_att6_Lq0_001_0001-1000/",
            
            # TODO: Uncomment and add your Globus Collection here
            # "from_storage_transfer_destination_endpoint_id": "6d3275c0-e5d3-11ec-9bd1-2d2219dcc1fa", 
            "from_storage_transfer_destination_path": str(data_dir),
            "from_storage_transfer_recursive": True,

            'metadata_file': input_hdf_file,
            'hdf_file': output_hdf_file,
            'execution_metadata_file': execution_metadata_file,

            # TODO: Uncomment and add your funcX endpoints here
            # "funcx_endpoint_non_compute": "",
            # "funcx_endpoint_compute": "",

            'boost_corr': {
                    'atype': 'TwoTime',
                    "qmap": qmap_file,
                    "raw": raw_file,
                    "output": output_dir,
                    "batch_size": 8,
                    "gpu_id": args.gpu_flag,
                    "verbose": False,
                    "masked_ratio_threshold": 0.75,
                    "use_loader": True,
                    "begin_frame": 1,
                    "end_frame": -1,
                    "avg_frame": 1,
                    "stride_frame": 1,
                    "overwrite": True,
            },
        }
    }

    corr_flow = XPCSBoost()
    flow_run = corr_flow.run_flow(flow_input=flow_input, label=run_label, tags=['gladier','demo', 'xpcs'])

    print('run_id : ' + flow_run['action_id'])