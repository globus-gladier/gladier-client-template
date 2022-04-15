class BaseDeployment:
    globus_endpoints = dict()
    funcx_endpoints = dict()
    flow_input = dict()

    def get_input(self):
        fi = self.flow_input.copy()
        fi['input'].update(self.funcx_endpoints)
        fi['input'].update(self.globus_endpoints)
        return fi

class SimpleDep(BaseDeployment):
    funcx_endpoints = {
        'funcx_endpoint_non_compute' : 'xxx',
        'funcx_endpoint_compute'     : 'yyy'
    }
    flow_input = {
        'input': {
            'search_index' : 'zzz',
        }
    }


deployment_map = {
    'client-test': SimpleDep(),
}
