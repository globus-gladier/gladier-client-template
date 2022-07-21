#!/usr/bin/env python

# Enable Gladier Logging
# import gladier.tests

import argparse
import os

from gladier import GladierBaseClient, generate_flow_definition

from tools.ptychodus_plot import PtychodusPlot

@generate_flow_definition(
    modifiers={
        "publish_gather_metadata": {
            "WaitTime": 240,
            "payload": "$.PtychodusPlot.details.result[0].pilot",
        },
    }
)
class PtychodusFlow(GladierBaseClient):
    gladier_tools = [
        "gladier_tools.globus.transfer.Transfer:FromStorage",
        "gladier_tools.posix.shell_cmd.ShellCmdTool",
        PtychodusPlot,
    ]



def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--datadir", help="input file pathname", default="~/gladier_demo/ptycho/")
    parser.add_argument("--samplename", help="input file pathname", default="demo1")
    return parser.parse_args()


if __name__ == "__main__":

    args = arg_parse()

    sample_name = args.samplename
    data_dir = os.path.join(args.datadir, sample_name)
    run_label = "DEMO Ptycho: " + sample_name

    # Base input for the flow
    flow_input = {
        "input": {
            # processing variables
            "sample_name": sample_name,
            "data_dir": data_dir,  # relative to endpoint
            "proc_dir": data_dir,  # relative to funcx

            # REMOTE DEMO ENDPOINT FOR PTYCHO DATA
            "from_storage_transfer_source_endpoint_id": "a17d7fac-ce06-4ede-8318-ad8dc98edd69", 
            "from_storage_transfer_source_path": "/PTYCHO/fly001",
            
            # LOCAL LAPTOP FOR DEMO
            ## TO DO: Add your own GCP UUID.
            "from_storage_transfer_destination_endpoint_id": "6d3275c0-e5d3-11ec-9bd1-2d2219dcc1fa", 
            "from_storage_transfer_destination_path": str(data_dir),
            "from_storage_transfer_recursive": True,

            # shell cmd inputs
            "args": f"ptychodus -f {data_dir} -b -s ptychodus.ini > ptychodus.log",
            "cwd": f"{data_dir}",
            "timeout": 180,
            
            # funcX endpoints
            "funcx_endpoint_non_compute": "",
            "funcx_endpoint_compute": "",
        }
    }

    ptycho_flow = PtychodusFlow()
    flow_run = ptycho_flow.run_flow(flow_input=flow_input, label=run_label)
    print("run_id : " + flow_run["action_id"])