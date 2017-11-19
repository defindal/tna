import json
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
import xml.etree.ElementTree as ET
import random

tree = ET.parse('alqaeda.xml')
root = tree.getroot()

xmlstr = ET.tostring(root, encoding='UTF-8', method='xml')

#print (json.dumps(bf.data(fromstring(xmlstr)),indent=4))

jsonData = bf.data(fromstring(xmlstr))

data = {}
data['nodes'] = []

for ind in jsonData['CONSOLIDATED_LIST']['INDIVIDUALS']['INDIVIDUAL']:

    newNode =  ind['FIRST_NAME']['$'] + ' '
    if('SECOND_NAME' in ind): newNode += ind['SECOND_NAME']['$'] + ' '
    if('THIRD_NAME' in ind): newNode += ind['THIRD_NAME']['$'] + ' '
    if('FOURTH_NAME' in ind): newNode += ind['FOURTH_NAME']['$'] + ' '
    print (ind['COMMENTS1']['$'])

    data['nodes'].append({
        'id': newNode,
        'score': 0,
        'note' : ind['COMMENTS1']['$']
    })

data['links'] = []

for node in (data['nodes']):
    x = random.randint(0,len(data['nodes'])-1)
    y = random.randint(0,len(data['nodes'])-1)

    if x != y:
        data['links'].append({
            'source' : data['nodes'][x]['id'],
            'target' : data['nodes'][y]['id'],
            'weight' : random.randint(1,20)

        })

#with open('alqaeda.json', 'w') as outfile:
#    json.dump(bf.data(fromstring(xmlstr)),outfile)

with open('terr.json', 'w') as outfile:
    json.dump(data, outfile)