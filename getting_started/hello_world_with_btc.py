import os
from btc_rest_api import EPRestApi

ep = EPRestApi()

# Create empty profile
response = ep.post_req('profiles?discardCurrentProfile=true')
print(f'{response}: {response.reason}')

# Add a message
payload = { "message": "Hello World from the BTC REST API!", "severity": "INFO" }
response = ep.post_req('messages', payload)
print(f'{response}: {response.reason}')

# Add a second message
payload = { "message": "This is another message", "severity": "ERROR" }
response = ep.post_req('messages', payload)
print(f'{response}: {response.reason}')

# Retrieve and print the messages
response = ep.get_req('messages')
messages = response.json()
print(messages)

#
# Bonus steps for early finishers
#

# Delete the second message
second_message_uid = messages[1]['uid']
response = ep.delete_req(f'messages/{second_message_uid}')
print(f'{response}: {response.reason}')

# Retrieve and print the messages again
response = ep.get_req('messages')
print(f'{response}: {response.reason}')
messages = response.json()
print(messages)

# Save the *.epp file
payload = { "path": os.path.abspath("profile.epp") }
response = ep.put_req('profiles', payload)
print(f'{response}: {response.reason}')
