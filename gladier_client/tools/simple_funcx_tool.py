from gladier import GladierBaseTool, generate_flow_definition


def example_function(**data):
    import os
    wfile = data['file']
    text = data['text']

    if '~' in wfile:
        wfile = os.path.expanduser(wfile)

    with open(wfile,"w") as file1:
        file1.writelines(text)

    return wfile

@generate_flow_definition
class ExampleTool(GladierBaseTool):
    funcx_functions = [example_function]
    required_input = [
        'file',
        'text', 
        'funcx_endpoint_compute'
        ]
