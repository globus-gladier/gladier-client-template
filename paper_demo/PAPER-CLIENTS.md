# Gladier Client Examples

Our paper presents 5 clients

* [XPCS]()
* [SSX]()
* [HEDM]()
* [BRAGGNN]()
* [PTYCHOGRAPHY]()

Although each has its own particular set of tools, much of the infrastructure is shared and can be installed follow the PAPER-HOW-TO.md manual.

## Test Data

Some public datasets can be found at this [globus endpoint](https://app.globus.org/file-manager?origin_id=a17d7fac-ce06-4ede-8318-ad8dc98edd69&origin_path=%2F~%2F).

a17d7fac-ce06-4ede-8318-ad8dc98edd69

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
