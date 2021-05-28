from gladier import GladierBaseTool


def tar(data):
    import os
    import tarfile
    tar_input = data['tar_input']
    if '~' in tar_input:
        tar_input = os.path.expanduser(tar_input)

    tar_output = data.get('tar_output', f'{tar_input}.tgz')
    with tarfile.open(tar_output, "w:gz") as tf:
        tf.add(tar_input)
    return tar_output


class Tar(GladierBaseTool):

    # Custom flow definition to set 'ExceptionOnActionFailure' to True. We don't
    # want a transfer to start if tarring fails
    flow_definition = {
        'Comment': 'Flow with states: Tar a given folder',
        'StartAt': 'Tar',
        'States': {
            'Tar': {
                'ActionUrl': 'https://api.funcx.org/automate',
                'Comment': None,
                'ExceptionOnActionFailure': True,
                'Parameters': {
                    'tasks': [
                        {
                            'endpoint.$': '$.input.funcx_endpoint_compute',
                            'func.$': '$.input.tar_funcx_id',
                            'payload.$': '$.input'
                        }
                    ]
                },
                'ResultPath': '$.Tar',
                'Type': 'Action',
                'WaitTime': 300,
                'End': True,
            },
        }
    }

    funcx_functions = [tar]
    required_input = [
        'tar_input', 
        'funcx_endpoint_non_compute'
        ]
