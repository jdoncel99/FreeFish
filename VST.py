import json
import requests

api_url = 'https://www.virustotal.com/vtapi/v2/url/report'
params = dict(apikey='fc06e14f7e9409d28771c645456c958477fb78eda4d89034bc1bde729827f2af', resource='https://brain-upd.com/programming/how-to-use-virustotal-api-with-python/', scan=0)
response = requests.get(api_url, params=params)
if response.status_code == 200:
  result=response.json()
  print(json.dumps(result, sort_keys=False, indent=4))
