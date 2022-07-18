# Infrastructure for Automation

The basic infrastructure needs to be set for three different data sites. The _local_ where the data starts, the _remote_ where data will be transfered and processed and the _portal_ where the results will be served to the portal.

Note that we do not define where the flow will be triggered. This is due the fact that once a flow is defined, it can be executed from "anywhere" and it will invoke the actions on the specified endpoints.

For the sake of simplicity we will use the _local_ computer as both execution and initial data endpoint. 

For data, three endpoints need to be defined:
* local data endpoint
* remote data endpoint
* portal data endpoint

For processing, we will define two endpoints, one to execute "cheap" operations on the head node of our facility and one that executes "expensive" operations and require the use of a queue.

* funcx_endpoint_non_compute
* funcx_endpoint_compute

## Local PC

* Install globus services?

* Globus Connect 
  * Install GCP (if not installed) 
  * Check GCP UUID
  * Check paths

## Remote PC

* Check GCP endpoint
  * Install GCP (if not installed)
* Check local path

* Install FuncX endpoints
  * Configure funcx endpoints

* Install required packages for computation

## Running the client

* Initial auth
* Check payload

## Creating the client

* Initial data flow
