from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
import config
import json
import name_tools

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID


class NameSuspicious(Resource):
    def get(self,name):
        print(name)

        t = 0.1
        with open(config.database) as json_file:
            data = json.load(json_file)

            for p in data['nodes']:
                dist = name_tools.match(p['id'],name)
                if dist > t: t = dist


        return t * 10



api.add_resource(NameSuspicious, '/checkName/<name>')  # Route_2
api.add_resource(Employees, '/employees')  # Route_1

print (app.url_map)

if __name__ == '__main__':
    app.run(port='5002')
