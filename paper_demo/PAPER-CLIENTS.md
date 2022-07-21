# Gladier Client Examples

Our paper presents 5 clients

* [XPCS]()
* [SSX]()
* [HEDM]()
* [BRAGGNN]()
* [PTYCHOGRAPHY]()

Although each has its own particular set of tools, they share common patterns and leverage the same services. Initial setup can be installed follow the PAPER-HOW-TO.md manual.

## Test Data

By default, test data is pulled from [globus endpoint](https://app.globus.org/file-manager?origin_id=a17d7fac-ce06-4ede-8318-ad8dc98edd69&origin_path=%2F~%2F). Data is available for
XPCS, SSX, and ptychography.

## Gladier Setup

Gladier is used to register FuncX functions and deploy flows. Below are the steps to
setup funcX endpoints. After this, running the test client below
will be possible. The test client, unlike the scientific tools, requires no additional external dependencies.

```bash

# Install the necessary components
conda create -n gladier_demo_remote python=3.9
conda activate gladier_demo_remote
pip install gladier funcx-endpoint

# Setup your FuncX "login" endpoint - this is used for organization tasks
# Use the generated UUID for "funcx_endpoint_non_compute" states
funcx-endpoint configure login
funcx-endpoint start login

# Setup your FuncX "compute" endpoint - this is typically used for computationally expensive tasks
# Use the generated UUID for "funcx_endpoint_compute" states
funcx-endpoint configure compute
funcx-endpoint start compute
```

You will need to edit the test_client.py script to include your
FuncX endpoints, along with a Globus Collection. Note: Your
FuncX endpoints _must_ have access to the Globus Collection you use.


Test your basic setup by running the test_client.py:

```bash

python test_client.py
```

Running the test client will prompt you to login and will direct you to the running flow in the Globus Web app.

If the run is successful, you are ready to try one of the other experiments.

## Installing the processing environment

To run flows that perform the various use cases we need to install domain specific tools in the processing conda environment. This will allow
the flow to execution functions that process the data. 

Note: you can reuse the conda environment previously created. After installation, you will need to restart your funcX endpoint.

```bash
#XPCS flow
conda install -c nvidia cudatoolkit
conda install -c pytorch pytorch
pip install -e git+https://github.com/AZjk/boost_corr#egg=boost_corr

#Ptycho tools
git clone https://github.com/AdvancedPhotonSource/ptychodus
cd ptychodus
conda install -c conda-forge --file requirements-dev.txt
conda install -c conda-forge tike
pip install -e . 
```

You may also want to modify your funcX endpoint configuration to provision compute nodes, if available. 

Several configuration examples can be found at the [funcx endpoints documentation](https://funcx.readthedocs.io/en/latest/endpoints.html).

Once installed and configured you will need to restart your funcX endpoints. 


## Running the use cases

You should now be able to run the various use case clients.

### Ptychography flow

The ptychography flow uses a shell command tool to execute the `ptychodus` tool on the example data.

To run the ptychography flow you will need to edit `ptychodus_client.py` to specify your endpoints and data paths.

```bash

python ptychodus_client.py --datadir <data path>
```

### XPCS flow

To run the XPCS flow you will need to edit `xpcs_client.py` to specify your endpoints.

```bash

python xpcs_client.py --datadir <data path>
```