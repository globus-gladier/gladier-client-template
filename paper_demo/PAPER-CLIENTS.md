# Gladier Client Examples



“For application experience, the five use cases does cover the broad spectrum of scenario, but it feels like the “flow” and bigger pictures were lost in translation. 
I suggest provide details on one of application use case with more cohesive step-by-step flow/actions, maybe in a table: 
- what does experiment scientists need to facilitate? 
- what does HPC facility need to deploy and provide interface with? 
- what does experimental facility/instrument needs to deploy or interface? 
- Which “discrete” steps can be automated by Gladier? 
- which can’t and require customization or manual intervention?”

Our paper presents 5 clients

* [XPCS]()
* [SSX]()
* [HEDM]()
* [BRAGGNN]()
* [PTYCHOGRAPHY]()

Although each has its own particular set of tools, much of the infrastructure is shared and can be installed follow the PAPER-HOW-TO.md manual.

## Test Data

By default, test data is pulled from [globus endpoint](https://app.globus.org/file-manager?origin_id=a17d7fac-ce06-4ede-8318-ad8dc98edd69&origin_path=%2F~%2F). Data is available for
XPCS, SSX, and ptychography.

## Gladier Setup

Gladier is used for registering FuncX functions and deploying flows. Below are steps to
setup funcx-endpoints and a Globus Collection. After this, running the test client below
will be possible. The test client, unlike the scientific tools, requires no additional external dependencies.

```bash

# Install the necessary components
conda create -n gladier_demo_remote python=3.9
conda activate gladier_demo_remote
pip install gladier funcx-endpoint

# Setup your FuncX "login" endpoint
# Use the generated UUID for "funcx_endpoint_non_compute" states
funcx-endpoint configure login
funcx-endpoint start login

# Setup your FuncX "compute" endpoint
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

If the run is successful, you are ready to try one of the other experiments.

## Installing the processing environment

```bash
conda create -n gladier_demo_remote python=3.8
conda activate gladier_demo_remote

pip install funcx-endpoint

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

The next step is to configure our funcx endpoints to start the correct processing environment.
on `~/.funcx/funcx_endpoint_non_compute/config.py` you need to add the variable `worker_init` to your provider.
In my case it looks like this:
```
provider=LocalProvider(
  worker_init='conda activate gladier_demo_remote',                                  init_blocks=1,                                                                      min_blocks=0,                                                                       max_blocks=1,                                                                   ),  
```

Several configuration examples can be found at the [funcx endpoints documentation](https://funcx.readthedocs.io/en/latest/endpoints.html).

And same for the compute endpoint. 
Restart your endpoints to get the new configuration.

## Installing the local environment

```bash
conda create -n gladier_demo_local python=3.8
conda activate gladier_demo_local

pip install gladier
mkdir gladier_demo
cd gladier_demo

#XPCS client
git clone https://github.com/globus-gladier/gladier-client-template
```
