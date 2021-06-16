import json

def dados():
  
	f = open ('dados.json', "r")
	data = json.loads(f.read())

	"""
	for i in data['items']:
		print(i['product']['name'])
	"""
	
	f.close()
	return json.dumps(data)

print(dados())
