from gladier import GladierBaseTool, generate_flow_definition

def xpcs_boost_corr(**data):
    import os
    import json
    import logging
    from boost_corr.xpcs_aps_8idi import gpu_corr_multitau, gpu_corr_twotime
    from boost_corr import __version__ as boost_version

    if not os.path.exists(data['proc_dir']):
        raise NameError(f'{data["proc_dir"]} \n Proc dir does not exist!')

    os.chdir(data['proc_dir'])

    log_file = os.path.join(data['proc_dir'], 'boost_corr.log')
    
    level = 'DEBUG' if data['boost_corr'].get('verbose') else 'INFO'
    
    handlers = (
        # Useful for flows, logging will be captured in a file
        logging.FileHandler(filename=log_file, mode='w'),
        # Useful for testing, will only output when run directly on compute
        logging.StreamHandler(),
    )
    logging.basicConfig(handlers=handlers, level=level)
    logging.info(f'Logging setup with level {level}')


    atype = data['boost_corr'].pop('atype')


    if atype in ('Multitau', 'Both'):
        gpu_corr_multitau.solve_multitau(**data['boost_corr'])
    elif atype in ('Twotime', 'Both'):
        gpu_corr_twotime.solve_twotime(**data['boost_corr'])

    
    metadata = {
        'executable' : {
            'name': 'boost_corr',
            'tool_version': str(boost_version),
            'device': 'gpu' if data['boost_corr'].get('gpu_flag', 0) >= 0 else 'cpu',
            'source': 'https://pypi.org/project/boost_corr/',
            }
    }

    if data.get('execution_metadata_file'):
        with open(data['execution_metadata_file'], 'w') as f:
            f.write(json.dumps(metadata, indent=2))
    logs = []
    if os.path.exists(log_file):
        with open(log_file) as f:
            logs = f.readlines()

    return {
        'result': 'SUCCESS',
        # 'boost_corr_log': logs,
        'proc_dir': data['proc_dir'],
        'boost_corr': data['boost_corr'],
    }


@generate_flow_definition(modifiers={
    xpcs_boost_corr: {'WaitTime': 7200, 'ExceptionOnActionFailure': True}
})
class BoostCorr(GladierBaseTool):

    required_input = [
        'proc_dir',
        'funcx_endpoint_compute',
    ]

    funcx_functions = [
        xpcs_boost_corr
    ]


if __name__ == '__main__':
    data = {
        'proc_dir':'/home/raf/gladier_demo/xpcs/demo1/',
        'boost_corr': {
            'raw':'A001_Aerogel_1mm_att6_Lq0_001_00001-01000.imm',
            'qmap':'comm201901_qmap_aerogel_Lq0.h5',
            'verbose':True,
            'atype': 'TwoTime',
            'output': 'output/',
            'batch_size': 8,
            'gpu_id': -1,
            'verbose': True,
            'masked_ratio_threshold': 0.75,
            'use_loader': True,
            'begin_frame': 1,
            'end_frame': -1,
            'avg_frame': 1,
            'stride_frame': 1,
            'overwrite': False
        }
    }
    
    xpcs_boost_corr(**data)
