# gladier-client-template


## Installing

    conda create -n gladier-test python=3.8 pip ipython jupyter
    conda activate gladier-test
    pip install funcx==0.0.5
    pip install globus_automate_client

    git clone https://github.com/globus-gladier/gladier-client-template
    cd gladier-client-template
    python setup.py develop

## Creating a new gladier client

- Start your repo with globus-gladier/gladier-client-template as template
- change the gladier-client folder to reflect your new name
- change the setup.py to reflect your new name

## Running

Try our notebooks 

- basic_funcx_flow
- gladier_demo_client

## Todo 

- Create rename.sh script to automate the template creation
- Can we do that at github workflows?