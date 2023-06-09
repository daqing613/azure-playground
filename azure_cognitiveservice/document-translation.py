import requests

endpoint = 'https://xxxxx.cognitiveservices.azure.com/'
key =  'xxxxxxxxxxxxxxxxxxx'
path = 'translator/text/batch/v1.0/batches'
constructed_url = endpoint + path

sourceSASUrl = 'https://xxxxx.blob.core.windows.net/source'

targetSASUrl = 'https://xxxxx.blob.core.windows.net/dest'

body= {
    "inputs": [
        {
            "source": {
                "sourceUrl": sourceSASUrl,
                "storageSource": "AzureBlob",
                "language": "zh-Hans"
            },
            "targets": [
                {
                    "targetUrl": targetSASUrl,
                    "storageSource": "AzureBlob",
                    "category": "general",
                    "language": "en"
                }
            ]
        }
    ]
}
headers = {
  'Ocp-Apim-Subscription-Key': key,
  'Content-Type': 'application/json',
}

response = requests.post(constructed_url, headers=headers, json=body)
response_headers = response.headers

print(f'response status code: {response.status_code}\nresponse status: {response.reason}\n\nresponse headers:\n')

for key, value in response_headers.items():
    print(key, ":", value)