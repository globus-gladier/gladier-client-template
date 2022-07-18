from gladier import GladierBaseTool, generate_flow_definition

def ptychodus_plot(**data):
    import os
    import subprocess
    import numpy as np
    import matplotlib.pyplot as plt

    proc_dir = data['proc_dir']

    npz_file = 'ptychodus.npz'

    os.chdir(proc_dir) 

    raw_data = np.load(npz_file)
    data_object = raw_data['object']
    data_probe = raw_data['probe']
    pixel_size = raw_data['pixelSizeInMeters']

    plt.imsave('object_real.jpg', data_object.real)
    plt.imsave('object_im.jpg', data_object.imag)

    plt.imsave('probe_0_real.jpg', data_probe[0,:,:].real)
    plt.imsave('probe_0_im.jpg', data_probe[0,:,:].imag)
    # plt.imsave('probe_1.jpg', data_probe[1,:,:])
    # plt.imsave('probe_2.jpg', data_probe[2,:,:])
    # plt.imsave('probe_3.jpg', data_probe[3,:,:])
    # plt.imsave('probe_4.jpg', data_probe[4,:,:])



    data['pilot']['dataset'] = data['upload_dir']
    data['pilot']['index'] = data['search_index']
    data['pilot']['project'] = data['search_project']
    data['pilot']['source_globus_endpoint'] = data['source_globus_endpoint'] ##Review this later
    data['pilot']['groups'] = data.get('groups',[])

    metadata = {}
    metadata.update({
        'sample_name': data['sample_name'],
#        'pixel_size': pixel_size
    })
    data['pilot']['metadata'] = metadata

    return {
        'pilot': data['pilot']
    }


@generate_flow_definition(modifiers={
    'ptychodus_plot': {'WaitTime':7200}
})
class PtychodusPlot(GladierBaseTool):
    flow_input = {}
    required_input = [
        'proc_dir',
        'funcx_endpoint_compute',
    ]
    funcx_functions = [ptychodus_plot]
