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

# Your Journey starts here.
## If you chose to accept it.

Hello traveler, this is your tutorial into the world of automation.

This repository is designed to be a guide through the complexities of Gladier and its tools.
For full automation of an experiment, there is a step of infrastructure that cannot be ignored. This is usually done once and allows the user to focus on tool development.

Three main operations are included on the simpleClients:
* Process
* Transfer
* Publish

## Installing Gladier

To run this tutorial we advise that a new environment is created on your favorite tool. For simplicity, we will use miniconda although any development app with access to pip should suffice.

    conda create -n gladier-test python pip
    conda activate gladier-test
    pip install gladier

## First run on a Gladier Client

Our first example can be found at `example_client/example_client.py`. It creates and executes a flow with one operation.

   ./example_client/example_client.py

To execute a remote function (the equivalent of a `lambda`) we use the funcX service to register, retrieve and execute functions. The service requires that a small instance client is deployed at the "processing" machine. We have a client running at one of our example machines. The location of this client is defined by:

    'funcx_endpoint_compute': '4b116d3c-1703-4f8f-9f6f-39921e5864df'

Note1: The remote machine is not necessary remote. Different parts of the flow can be executed on different machines by changing the `funcx_endpoint_compute` value for each tool. This will be explored on a further section.

Note2: Gladier reads the python function imported by `SimpleTool` and automatically register or re-register(in the case of changes in the local function definition) it with the funcx service. The UUID of this function is automatically populated in the flow definition. 


During the execution takes care of creating the flow definition and registering it with the globus service:

    Flow created with ID: ddb9d6be-d48f-40df-a663-6bcc6db1bb76                                                              https://app.globus.org/flows/ddb9d6be-d48f-40df-a663-6bcc6db1bb76 

And also created the run after the `.run()` execution:

    Run started with ID: 6fa0969a-2778-4f7f-95d5-d365e89aca32                                                               https://app.globus.org/runs/6fa0969a-2778-4f7f-95d5-d365e89aca32 

Running the client again will not register a new flow with the globus service but will generate a new run instance.

### Best Practices: 
The `SimpleTool` and its driving function `simple_function` are separated into a `tools` folder in a single file. We advise to create one python file per "action" in the flows. This makes development and debugging and tracing errors much simpler.

The `example_client.py` itself also is separated from the other clients in the folder and only contain one `GladierBaseClient`. This prevents instances being created with the 'wrong' flow definition or common mistakes on 'what is running'.


## Creating a flow with Transfer

Our second example can be found at `example_client/example_client_transfer.py`. It transfer a file from our remote server into your workstation. 
In order to allow for transfer, the first step is to introduce the workstation in the the creates and executes a flow with one operation.

   ./example_client/example_client_transfer.py


## Creating a flow with Publish

Our Third example can be found at `example_client/example_client_publish.py`. It do a simple operation of publishing some data into a globus index.
As before, it requires the setup of a globus index and how to visualize it. 

    pip install globus-search-cli
    globus-search login
    globus-search index create example-index gladier-example-index

The result is a new search index on the globus-search database which will serve as a "repository" for the flow data.

    {
       "@datatype": "GSearchIndex",
       "@version": "2017-09-01",
       "creation_date": "2022-04-27 21:04:30",
       "description": "gladier-example-index",
       "display_name": "example-index",
       "id": "563c3d98-6fa8-4ef5-83e2-0f378efe0a5f",
       "is_trial": true,
       "max_size_in_mb": 1,
       "num_entries": 0,
       "num_subjects": 0,
       "size_in_mb": 0,
       "status": "open",
       "subscription_id": null
    }    

The search index id `563c3d98-6fa8-4ef5-83e2-0f378efe0a5f` will be used so the flow knows where to send metadata too.

To execute our simple publish client

   ./example_client/example_client_publish.py

To check if the data went to the index try this check https://acdc.alcf.anl.gov/globus-tutorial/563c3d98-6fa8-4ef5-83e2-0f378efe0a5f


## Making this template into a client

    ./scripts/create_setup.py

## Installing gladier_client

    conda create -n gladier pip
    conda activate gladier

    git clone https://github.com/globus-gladier/gladier-client-template
    cd gladier-client-template
    
    pip install -r requirements.txt

    python setup.py develop
