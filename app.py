from flask import Flask, jsonify
import os, copy


app = Flask(__name__)

person1 = {
    "id": 1,
    "first_name":"Enrique",
    "last_name": "Smith",
    "age":29,
    "parents":[2,3],
    "kid":[]
}

person2 = {
    "id": 2,
    "first_name":"Mom",
    "last_name": "Smith",
    "age":55,
    "parents":[],
    "kid":[1,4,5,6,7]
}

person3 = {
    "id": 3,
    "first_name":"Dad",
    "last_name": "Smith",
    "age":58,
    "parents":[],
    "kid":[1,4,5,6,7]
}

person4 = {
    "id": 4,
    "first_name":"Sister1",
    "last_name": "Smith",
    "age": 35,
    "parents":[2,3],
    "kid":[]
}

person5 = {
    "id": 5,
    "first_name":"Sister2",
    "last_name": "Smith",
    "age": 33,
    "kid":[],
    "parents":[2,3]
}

person6 = {
    "id": 6,
    "first_name":"Brother1",
    "last_name": "Smith",
    "age": 27,
    "kid":[],
    "parents":[2,3]
}

person7 = {
    "id": 7,
    "first_name":"Brother2",
    "last_name": "Smith",
    "age": 25,
    "kid":[],
    "parents":[2,3]
}


family={
    "members": [person3, person2, person4, person5, person1, person6, person7]
}

def getElement(a):
    for i in family["members"]:
        if a == i["id"]:
            return i


@app.route('/')
def index():
    return jsonify(family)

@app.route('/member/<int:id>')
def get_member(id):
    if id > 0:
        print(family["members"])
        for i in family["members"]:
            if id == i["id"]:
                ele = copy.deepcopy(i)
                print(ele)
                x = ele["parents"]
                y = ele["kid"]
                temporList = []
                tempList = []
                for n in x:
                    tempList.append(getElement(n))
                ele["parents"] = tempList
                for m in y:
                    temporList.append(getElement(m)) 
                ele["kid"] = temporList
                
                
                return jsonify({"status_code": 200, "data": ele})
    
            
        response = jsonify({"error": 400, "message":"no member found" })
        response.status_code = 400
        return response



app.run(host='0.0.0.0', port=os.environ.get('PORT'))