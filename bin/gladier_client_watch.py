from gladier import GladierBaseClient



@generate_flow_definition
class Example_Client(GladierClient):
    gladier_tools = [
        'gladier_tools.globus.Transfer'
        'gladier_tools.posix.Tar'
#        'gladier_tools.globus.Transfer'
    ]

def ClientLogic(event_file):

    client_zip_flow = kanzus_workshop_client.start_flow(flow_input=flow_input)
    print("  Trigger : " + base_input["input"]["trigger_name"])
    print("  Range : " + base_input["input"]["input_range"])
    print("  UUID : " + client_zip_flow['action_id'])
    print('')




def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--single", help="Single File Transfer", default=None)
#    parser.add_argument("--watch", help="Folder to watch", default=None)
    args = parser.parse_args()


if __name__ == '__main__':


    args = parse_args()
    single = args['single']
    watch = args['']

    if single & watch:
        print('Choose only one option')
        return

    ##parse dirs
    local_dir = args.localdir
    data_dir = args.datadir
    
    ##Process endpoints - theta
    dest_funcx_endpoint = '8f2f2eab-90d2-45ba-a771-b96e6d530cad'
    ##Transfer endpoints - 
    local_globus_endpoint='87c4f45e-9c8b-11eb-8a8c-d70d98a40c8d'
    dest_globus_endpoint='08925f04-569f-11e7-bef8-22000b9a448b'

    

    stills_cont_fxid = register_container() ##phase out with containers

    base_input = {
        "input": {
            #Processing variables
            "local_dir": local_dir,
            "transfer_file": data_dir,

            # funcX endpoints
            "funcx_dest_ep": dest_funcx_endpoint,

            # globus endpoints
            "globus_local_ep": local_globus_endpoint,
            "globus_dest_ep": dest_globus_endpoint, 
        }
    }

    exampleClient = Example_Client()

    if watch: 
        exp = GladierTriggers(local_dir)
        exp.run()
    else:

