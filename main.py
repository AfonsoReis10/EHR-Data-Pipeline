import json
import psycopg2
from psycopg2.extras import Json
from collections import Counter


with open(r"\output\fhir\Carlton317_Greenfelder433_00775e7f-4f38-d6ac-106b-4fd36072bd54.json", 'r') as file:
    data = json.load(file)

# Patient resource
patient = data['entry'][0]['resource']

#Patient data
name = patient.get('name')[0]
given_name = [nome for nome in name.get('given')]
full_given_name = " ".join(given_name)
family_name = name.get('family')
id = patient.get('id')
gender = patient.get('gender')
birthDate = patient.get('birthDate')
address = patient.get('address')[0]
city = address.get('city')
state = address.get('state')
country = address.get('country')
postalCode = address.get('postalCode')
maritalStatus = patient.get('maritalStatus').get('text')


print(given_name)
print(family_name)
print(full_given_name)



types = [e['resource']['resourceType'] for e in data['entry']]
print(Counter(types))


