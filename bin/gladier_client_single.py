#!/usr/bin/env python

from gladier import GladierBaseClient, generate_flow_definition
from pprint import pprint
import  os


@generate_flow_definition
class Example_Client(GladierBaseClient):
    gladier_tools = [
        'gladier_tools.globus.Transfer',
        'gladier_tools.posix.Tar',
    ]


if __name__ == '__main__':

    single = '/home/raf/workspace/demo/test.txt'

    if not single:
        "please provide a file for this example"

    ##parse dirs
    local_file = os.path.basename(single)
    local_dir = os.path.dirname(single)

    dest_file = ''
    dest_dir = '/home/ubuntu/demo'

    ##Local endpoints
    local_globus_endpoint='6edd58d2-bfdb-11eb-bddc-5111456017d9'

    ##Remote endpoints
    dest_funcx_endpoint = '2567415e-9bc3-4955-a498-3481f4c04248'
    dest_globus_endpoint='87c4f45e-9c8b-11eb-8a8c-d70d98a40c8d'


    base_input = {
        "input": {
            #Processing variables
            "transfer_source_path": os.path.join(local_dir,local_file),
            "transfer_destination_path": os.path.join(dest_dir,local_file),
            "tar_input": os.path.join(dest_dir,local_file),

            'transfer_recursive': False,

            'prime_threshould': 200,

            # funcX endpoints
            "funcx_endpoint_compute": dest_funcx_endpoint,

            # globus endpoints
            "transfer_source_endpoint_id": local_globus_endpoint,
            "transfer_destination_endpoint_id": dest_globus_endpoint, 
        }
    }

    print(base_input)

    exampleClient = Example_Client()

    example_flow = exampleClient.run_flow(flow_input=base_input)
    print("  File : " + base_input["input"]["transfer_source_path"])
    print("  UUID : " + example_flow['action_id'])

