from gladier import GladierBaseTool


def untar_file(data):
    import os
    import tarfile

    ##minimal data inputs payload
    file_path = data.get('file_path', '')
    file_name = data.get('file_name', '')
    output_path = data.get('output_path', '')
    ##

    full_path = os.path.join(file_path, file_name)

    if not os.path.isfile(full_path):
        raise NameError(f'{full_path}  does not exist!!')

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    with tarfile.open(full_path) as file:
        file.extractall(output_path)
    return output_path

class UnTar(GladierBaseTool):

    flow_definition = {
        'Comment': 'UnTar a single file',
        'StartAt': 'UnTar',
        'States': {
            'UnTar': {
                'ActionUrl': 'https://api.funcx.org/automate',
                'Comment': None,
                'ExceptionOnActionFailure': True,
                'Parameters': {
                    'tasks': [
                        {
                            'endpoint.$': '$.input.funcx_endpoint_non_compute',
                            'func.$': '$.input.untar_file_funcx_id',
                            'payload.$': '$.input'
                        }
                    ]
                },
                'ResultPath': '$.UnTar',
                'Type': 'Action',
                'WaitTime': 300,
                'End': True,
            },
        }
    }

    funcx_functions = [untar_file]

    required_input = [
        'file_path',
        'file_name',
        'output_path',
        'funcx_endpoint_non_compute'
        ]

