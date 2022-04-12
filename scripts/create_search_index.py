import pickle, base64, os, pprint, globus_sdk

# Name of the search index to use for this notebook
index_name = 'gladier-tutorial'

# Load a search client using a token from the Jupyterhub login
data = pickle.loads(base64.b64decode(os.getenv('GLOBUS_DATA')))
search_token = data['tokens']['search.api.globus.org']['access_token']
search = globus_sdk.SearchClient(authorizer=globus_sdk.AccessTokenAuthorizer(search_token))

# Fetch all indices a user has access
indices = [si for si in search.get("/v1/index_list").data['index_list']
           if si['is_trial'] 
           and si['display_name'] == index_name
           and 'owner' in si['permissions']
          ]

# If an index was found with the criteria above, re-use it. Otherwise,
# create a new index.
if indices:
    tutorial_index = indices[0]
    print('Found existing index!')
else:
    index_doc = {
        "display_name": index_name, 
        "description": 'A trial index for running my search tutorial'
    }
    tutorial_index = search.post("/beta/index", json_body=index_doc).data
    print('New search index created succcessfully.')

search_index = tutorial_index['id']

print(tutorial_index['display_name'])
print(tutorial_index['description'])