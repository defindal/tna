import json
import mockup as m
import config

def persist(sender,receiver,amount):
    with open(config.database) as json_file:
        data = json.load(json_file)

        if (not searchNode(data,sender)):addNode(data,sender)
        if (not searchNode(data,receiver)): addNode(data,receiver)

def addNode(data,newNode):

    data['nodes'].append({
        'id': newNode,
        'group': 0
    })

    with open(config.database, 'w') as outfile:
        json.dump(data,outfile)

def searchNode(data, needle):
    for p in data['nodes']:
        if p['id'] == needle:
            return True
    return False


persist(m.randomword(5),m.randomword(5),1000)
#addNode()