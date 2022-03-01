# gladier-client-template

## HOW TO USE THIS TEMPLATE

> **DO NOT FORK** this is meant to be used from **[Use this template](https://github.com/globus-gladier/gladier-client-template/generate)** feature.

1. Click on **[Use this template](https://github.com/globus-gladier/gladier-client-template/generate)**
2. Give a new name to your gladier project  
   (e.g. `gladier_amazing_science` recommendation is to use all lowercase and underscores separation for repo names.)
3. Wait until the first run of CI finishes  
   (Github Actions will process the template and commit to your new repo)
4. Then clone your new gladier and start tweaking it.

> **NOTE**: **WAIT** until first CI run on github actions before cloning your new project.

## Installing gladier_client

    conda create -n gladier pip
    conda activate gladier

    git clone https://github.com/globus-gladier/gladier-client-template
    cd gladier-client-template
    
    pip install -r requirements.txt

    python setup.py develop
