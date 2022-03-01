import datetime
import copy


class BaseDeployment:
    globus_endpoints = dict()
    funcx_endpoints = dict()
    flow_input = dict()

    def get_input(self):
        fi = self.flow_input.copy()
        fi['input'].update(self.funcx_endpoints)
        fi['input'].update(self.globus_endpoints)
        return fi

class BaseDeployment(BaseDeployment):

    globus_endpoints = {
        'globus_endpoint_source': '',
        'globus_endpoint_proc': '',
    }

    funcx_endpoints = {
        'funcx_endpoint_non_compute': '',
        'funcx_endpoint_compute': '',
    }

    flow_input = {
        'input': {
            'staging_dir': '/foo/bar',
        }
    }


deployment_map = {
    'base': BaseDeployment(),
}
