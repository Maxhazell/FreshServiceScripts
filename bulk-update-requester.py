import requests

ID = []
for x in ID:
    URL = "https://YOUR-DOMAIN.freshservice.com/api/v2/tickets/{}".format(x)

    headers = {
        'Content-Type': 'application/json',
    }

    json_data = {
        'requester_id': 123,
        'group_id': 1234,
        'category': 'Category',
    }

    response = requests.put(
        URL,
        headers=headers,
        json=json_data,
        auth=('YOUR-API-KEY', 'X'),
    )

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"requester_id" : 123, "group_id" : 1234, "category" : "Category" }'
#response = requests.put(
#    'https://YOUR-DOMAIN.freshservice.com/api/v2/tickets/',
#    headers=headers,
#    data=data,
#    auth=('YOUR-API-KEY', 'X'),
#)p