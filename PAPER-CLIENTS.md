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

## Installing the local environment

```bash
conda create -n gladier_demo_local python=3.8
conda activate gladier_demo_local

pip install gladier
mkdir gladier_demo
cd gladier_demo

#XPCS client
git clone https://github.com/globus-gladier/gladier-xpcs

#Ptycho tools
git clone https://github.com/globus-gladier/gladier-ptycho
```
