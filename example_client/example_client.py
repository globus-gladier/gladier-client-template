import argparse

from gladier import GladierBaseClient, generate_flow_definition

from tools.example_transfer import ExampleTransfer
from tools.simple_funcx_tool import SimpleTool

@generate_flow_definition
class Example_Client(GladierBaseClient):
    gladier_tools = [
        SimpleTool,
    ]


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', help='User Name', default='Bob')
    return parser.parse_args()


if __name__ == '__main__':

    args = arg_parse()

    flow_input = {
        'input': {
            'name': args.name, 
            'file' : '/test/test.txt',

            # funcX tutorial endpoint
            'funcx_endpoint_compute': '4b116d3c-1703-4f8f-9f6f-39921e5864df',
        }
    }

    exampleClient = Example_Client()

    client_run_label = 'ExampleGladierFlow'

    flow_run = exampleClient.run_flow(flow_input=flow_input, label=client_run_label)

    print('run_id : ' + flow_run['action_id'])
    print(flow_input)

