import os
import requests

# Create empty profile
response = requests.post('http://localhost:1337/ep/profiles')
print(response)

# Add a message
payload = { "message": "Hello World from the BTC REST API!", "severity": "INFO" }
response = requests.post('http://localhost:1337/ep/messages', json=payload)
print(response)

# Add a second message
payload = { "message": "This is another message", "severity": "ERROR" }
response = requests.post('http://localhost:1337/ep/messages', json=payload)
print(response)

# Retrieve and print the messages
response = requests.get('http://localhost:1337/ep/messages')
messages = response.json()
print(messages)

#
# Bonus steps for early finishers
#

# Delete the second message
second_message_uid = messages[1]['uid']
response = requests.delete(f'http://localhost:1337/ep/messages/{second_message_uid}')
print(response)

# Retrieve and print the messages again
response = requests.get('http://localhost:1337/ep/messages')
messages = response.json()
print(messages)

# Save the *.epp file
payload = { "path": os.path.abspath("profile.epp") }
response = requests.put('http://localhost:1337/ep/profiles', json=payload)
print(response)
