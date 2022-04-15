import argparse

from deployments import deployment_map
from gladier import GladierBaseClient, generate_flow_definition

#import tools
from tools.example_transfer import ExampleTransfer
from tools.simple_funcx_tool import SimpleTool

@generate_flow_definition
class Example_Client(GladierBaseClient):
    gladier_tools = [
#        ExampleTransfer,
        SimpleTool,
    ]


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--myname', help='User Name', default='Spark')
    parser.add_argument('--myage', help='User Age', default='42')
    parser.add_argument('--dep','-d', help='Deployment', default='client-test')
    return parser.parse_args()


if __name__ == '__main__':

    args = arg_parse()

    depl = deployment_map.get(args.dep)
    if not depl:
        raise ValueError(f'Invalid Deployment, deployments available: {list(deployment_map.keys())}')

    depl_input = depl.get_input()
 
    flow_input = {
        'input': {
            'my_name': args.myname, 
            'my_age': args.myage,
            'file' : '/test/',
            'text' : args.myname,

            # funcX endpoints
            'funcx_endpoint_non_compute': depl_input['input']['funcx_endpoint_non_compute'],
            'funcx_endpoint_compute': depl_input['input']['funcx_endpoint_compute'],

            # globus endpoints
#            'globus_endpoint_local': depl_input['input']['globus_endpoint_source'],
#            'globus_endpoint_remote': depl_input['input']['globus_endpoint_proc'],
        }
    }

    exampleClient = Example_Client()

    client_run_label = 'This is a test'

    flow_run = exampleClient.run_flow(flow_input=flow_input, label=client_run_label)

    print('run_id : ' + flow_run['action_id'])
    print(flow_input)

