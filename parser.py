import json
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring
import xml.etree.ElementTree as ET

tree = ET.parse('alqaeda.xml')
root = tree.getroot()

xmlstr = ET.tostring(root, encoding='UTF-8', method='xml')

#print (json.dumps(bf.data(fromstring(xmlstr)),indent=4))

jsonData = bf.data(fromstring(xmlstr))

for ind in jsonData['CONSOLIDATED_LIST']['INDIVIDUALS']['INDIVIDUAL']:
    print (ind['FIRST_NAME']['$'])
    if('SECOND_NAME' in ind): print(ind['SECOND_NAME']['$'])
    if('THIRD_NAME' in ind): print(ind['THIRD_NAME']['$'])
    if('FOURTH_NAME' in ind):print(ind['FOURTH_NAME']['$'])
    print (ind['COMMENTS1']['$'])

with open('alqaeda.json', 'w') as outfile:
    json.dump(bf.data(fromstring(xmlstr)),outfile)