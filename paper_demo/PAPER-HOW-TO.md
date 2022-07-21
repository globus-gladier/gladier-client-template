# Infrastructure for Automation

Our paper presents 5 clients [XPCS](), [SSX](), [HEDM](), [BRAGGNN]() and [PTYCHO]() to show the execution of scientific flows and automation of data processing.

Although each has its own particular set of tools, many share common patterns and infrastructure, allowing users to focus on customizing the domain specific parts. The initial configuration step (which may already be setup at some facilities) is to define the data endpoints. For our flows, we had three primary data location. _Local_ where the data starts, _remote_ where data will be transfered and processed, and _portal_ where the results will be served to facilitate visualization in a data portal.

Note that we do not define where the flow will be triggered. This is due the fact that once a flow is defined, it can be executed from anywhere and will invoke actions across the specified endpoints. For the sake of simplicity, here we use the _local_ computer as both execution and initial data endpoint.

Processing is achieved using a funcX endpoint. In order to optimize flow execution, we define two endpoints: one (where workers have network access) to execute organizational operations on login node of our facility and another that executes computationally expensive operations using HPC resources. Here, one can simply use a trivial endpoint for both tasks as the examples are not computationally expensive.

* funcx_endpoint_non_compute - to perform simple tasks
* funcx_endpoint_compute - to interface with HPC resources

We describe the basic installation of these endpoints and where they are integrated in a _flow_ definition.

## Configuration

Configuring your environment: We need a local Globus endpoint to move example datasets. This can be deployed yourself, or use an existing Globus Connect Personal or Globus Connect Server endpoint.
* Globus Connect 
  * Install GCP (if not installed) 
  * Check GCP UUID
  * Check paths

### Installing and Configuring your funcX endpoint

We recommend following the [funcX tutorial](https://funcx.readthedocs.io/en/latest/Tutorial.html
) to get familiriazed with the funcX platform. Here we install funcx-endpoint and start an endpoint to perform tasks.

  conda create -n demo_ep python=3.8
  conda activate demo_ep
  pip install funcx-endpoint
  funcx-endpoint configure funcx_endpoint_non_compute
  funcx-endpoint configure funcx_endpoint_compute

At this point you should have 2 folders created at `~/.funcx`, one for each endpoint.
We need to configure each of this endpoints for a particular functions. A list of example configurations can be found [here](funcx_ep_list).

  funcx-endpoint start funcx_endpoint_compute
  funcx-endpoint start funcx_endpoint_non_compute

  funcx-endpoint list 

should give you the uuid of this endpoints and those will be necessary for the clients.


## Running the client

* Initial auth
* Check payload

## Creating the client

* Initial data flow

