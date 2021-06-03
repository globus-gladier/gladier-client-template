# gladier-client-template


## Installing

    conda create -n gladier-test python=3.8 pip ipython jupyter
    conda activate gladier-test

    git clone https://github.com/globus-gladier/gladier-client-template
    cd gladier-client-template
    
    pip install -r requirements.txt

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