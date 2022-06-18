import urllib.request, json

try:
    url = "https://api.msil.go.jp/fishery/demarcated-fishery-right/v1/query?where='%E5%8C%97%E6%B5%B7%E9%81%93'&units=meter&returnGeometry=true"

    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'Ocp-Apim-Subscription-Key': '0e83ad5d93214e04abf37c970c32b641',
    }

    req = urllib.request.Request(url, headers=hdr)

    req.get_method = lambda: 'GET'
    response = urllib.request.urlopen(req)
    data = response.read()
    todo_item = json.loads(data)
    with open('result.json', 'w') as fp:
        json.dump(todo_item, fp, indent = "")
          
    #print(response.getcode())
    
except Exception as e:
    print(e)