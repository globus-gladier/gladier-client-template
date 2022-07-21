from gladier import GladierBaseClient, generate_flow_definition

@generate_flow_definition
class GladierTestClient(GladierBaseClient):
    gladier_tools = [
        "gladier_tools.globus.transfer.Transfer:FromStorage",
        "gladier_tools.posix.shell_cmd.ShellCmdTool",
    ]


if __name__ == "__main__":

    # The input data will be copied to this location for processing
    destination_path = "~/gladier_demo/ptycho/"

    # Base input for the flow
    flow_input = {
        "input": {

            # The Test data sourced from a public location. 
            "from_storage_transfer_source_endpoint_id": "a17d7fac-ce06-4ede-8318-ad8dc98edd69", 
            "from_storage_transfer_source_path": "/PTYCHO/fly001",
            
            # TODO: Uncomment and add your Globus Collection here
            # "from_storage_transfer_destination_endpoint_id": "", 
            "from_storage_transfer_destination_path": destination_path,
            "from_storage_transfer_recursive": True,

            # shell cmd inputs
            "args": f"ls {destination_path} > /dev/null && echo 'Execution Test Successful!'",
            "capture_output": True,
            
            # TODO: Add your FuncX endpoint here.
            "funcx_endpoint_compute": "",
        }
    }

    # Run the flow. If running this for the first time, it will prompt a login flow.
    gladier_test_client = GladierTestClient()
    run = gladier_test_client.run_flow(flow_input=flow_input, label=f'Gladier Test')
    print(f"Run started, you can also track the progress at: \n"
          f"https://app.globus.org/runs/{run['run_id']}")

    # Track the progress of the flow until completion
    gladier_test_client.progress(run["run_id"])

    # Report the result
    status = gladier_test_client.get_status(run["run_id"])
    if status.get("status") == "SUCCEEDED":
        print(status["details"]["output"]["ShellCmd"]["details"]["result"][0])
