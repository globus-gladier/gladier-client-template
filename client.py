from gladier import GladierBaseClient



class Example_Client(GladierClient):
    client_id = 'e6c75d97-532a-4c88-b031-8584a319fa3e'
    gladier_tools = [
        'gladier_tools.xpcs.EigenCorr',
        'gladier_tools.xpcs.ApplyQmap',
    ]

def ClientLogic(event_file):

    client_zip_flow = kanzus_workshop_client.start_flow(flow_input=flow_input)
    print("  Trigger : " + base_input["input"]["trigger_name"])
    print("  Range : " + base_input["input"]["input_range"])
    print("  UUID : " + client_zip_flow['action_id'])
    print('')




def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--watch", help="Folder to watch",
                    default=None)
    parser.add_argument("--single", help="Single File Transfer",
                    default=None)
    args = parser.parse_args()


if __name__ == '__main__':


