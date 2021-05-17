# Use your api.video api key to retrieve a new refresh token. You can use this token
# to get a new access token. Access tokens expire after one hour. You can also 
# use this to cancel an existing refresh token and replace it with a new one. 
# This is useful if your refresh token was compromised.

import apivideo

api_key = "your api key here"
client = apivideo.AuthenticatedApiClient(api_key)

# If you prefer to use the sandbox environment:
# client = apivideo.AuthenticatedApiClient(api_key, production=False)

client.connect()

# Refresh your token
client.refresh_token()

# You can view the object like this. Use this for reference and testing only.
print(client.__dict__)
