
##Process endpoints - theta
dest_funcx_endpoint = '2567415e-9bc3-4955-a498-3481f4c04248'
##Transfer endpoints - 
local_globus_endpoint='6edd58d2-bfdb-11eb-bddc-5111456017d9'
dest_globus_endpoint='87c4f45e-9c8b-11eb-8a8c-d70d98a40c8d'


base_input = {
    "input": {
        #Processing variables
        "transfer_source_path": os.path.join(local_dir,local_file),
        "transfer_destination_path": os.path.join(dest_dir,local_file),
        "tar_input": os.path.join(dest_dir,local_file),

        'transfer_recursive': False,

        # funcX endpoints
        "funcx_endpoint_compute": dest_funcx_endpoint,

        # globus endpoints
        "transfer_source_endpoint_id": local_globus_endpoint,
        "transfer_destination_endpoint_id": dest_globus_endpoint, 
    }
}


tar_uuid = 'd12148b9-cc6e-4591-a37e-a9c7e515801b'

res = fxc.run(endpoint_id=dest_funcx_endpoint, function_id=tar_uuid, payload=base_input['input'])
print(res)