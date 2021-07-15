import base64
from flask import Flask, render_template, request
from flask.wrappers import Request
import requests
import json
import sys
import string
import random
import base64

app = Flask(__name__)

calls = {
    "track": {
        "userId": "user123",
        "event": "Product Purchased",
        "properties": {
            "name": "Rubik's Cube",
            "revenue": 4.99,
        },
        "context": {
            "ip": "14.5.67.21"
        },
        "timestamp": "2020-02-02T00:23:09.544Z"
    },
    "identify": {
        "userId": "identified user id",
        "anonymousId": "anon-id-new",
        "context": {
            "traits": {
                "trait1": "new-val"
            },
            "ip": "14.5.67.21",
            "library": {
                "name": "http"
            }
        },
        "timestamp": "2020-02-02T00:23:09.544Z"
    },
    "page": {
        "userId": "identified user id",
        "anonymousId": "anon-id-new",
        "name": "Page View",
        "properties": {
            "title": "Home",
            "path": "/"
        },
        "context": {
            "ip": "14.5.67.21",
            "library": {
                "name": "http"
            }
        },
        "timestamp": "2020-02-02T00:23:09.544Z"
    },
    "screen": {
        "userId": "identified user id",
        "anonymousId": "anon-id-new",
        "name": "Screen View",
        "properties": {
            "prop1": "5"
        },
        "context": {
            "ip": "14.5.67.21",
            "library": {
                "name": "http"
            }
        },
        "timestamp": "2020-02-02T00:23:09.544Z"
    },
    "group": {
        "userId": "user123",
        "groupId": "group1",
        "traits": {
            "name": "Company",
            "industry": "Industry",
            "employees": 123
        },
        "context": {
            "traits": {
                "trait1": "new-val"
            },
            "ip": "14.5.67.21",
            "library": {
                "name": "http"
            }
        },
        "timestamp": "2020-01-21T00:21:34.208Z"
    },
    "alias": {
        "userId": "user123",
        "previousId": "previd1",
        "context": {
            "traits": {
                "trait1": "new-val"
            },
            "ip": "14.5.67.21",
            "library": {
                "name": "http"
            }
        },
        "timestamp": "2020-01-21T00:21:34.208Z"
    }
}


# this function will be called only if there is a list named userListDelete or userListAdd in properties of a track call
def random_user_generator(userList, size=0):
    fn = "abc"
    ln = "def"
    extern_id = "user"
    email1 = "abc"
    email2 = "@testmail.com"
    phone = "7685"
    ct = "Kolkata"
    st = "West Bengal"
    madid = "MOB"
    country = "India"
    for i in range(size):
        temp = random.randint(0, size)
        dict = {}
        dict["FN"] = fn + str(temp)
        dict["LN"] = ln + str(temp)
        dict["EXTERN_ID"] = extern_id + str(temp)
        dict["EMAIL"] = email1 + str(temp) + email2
        dict["PHONE"] = "7685"+''.join(random.choices(string.digits, k=6))
        dict["GEN"] = "M"
        dict["DOBY"] = str(1990 + i % 30)
        dict["DOBD"] = str((i % 30)+1)
        dict["DOBM"] = str((i % 11)+1)
        dict["FI"] = "ab"
        dict["CT"] = ct
        dict["ST"] = st
        dict["ZIP"] = ''.join(random.choices(string.digits, k=6))
        dict["MADID"] = madid + str(i)
        dict["COUNTRY"] = country
        userList.append(dict)
    return userList


def caller(url, headers, payload, size, calltype):
    payload_json = json.loads(payload)
    if calltype == "track":
        if "properties" in payload_json:
            # Checking if userListDelete or userListUpdate is there in the properties or not
            if "userListDelete" in payload_json["properties"] and isinstance(
                    payload_json["properties"]["userListDelete"], list):
                random_user_generator(
                    payload_json["properties"]["userListDelete"], size)
            if "userListAdd" in payload_json["properties"] and isinstance(
                    payload_json["properties"]["userListAdd"], list):
                random_user_generator(
                    payload_json["properties"]["userListAdd"], size)
    payload = json.dumps(payload_json, indent=4)
    size = str(sys.getsizeof(payload)/1024)  # finding size of payload
    response = requests.request("POST", url, headers=headers, data=payload)
    # return response.text
    return render_template("output.html", response=response.text, size=size, payload=payload)


@ app.route('/', methods=['POST', 'GET'])
def hello_world1():
    if request.method == "POST":
        if "call" in request.form:
            return render_template("index.html",
                                   data=json.dumps(
                                       calls[request.form["call"]]),
                                   data1=request.form["call"])
        elif request.form["payload"]:
            url = "http://localhost:8080/v1/" + request.form["calltype"]
            size = int(request.form["size"])
            payload = request.form["payload"]
            writekey = base64.b64encode((request.form["Writekey"] +
                                         ":").encode("ascii")).decode("ascii")
            headers = {
                'Content-Type': 'application/json',
                'Authorization': 'Basic ' + writekey
            }
            return caller(url, headers, payload, size,
                          request.form["calltype"])
        else:
            return render_template('index.html')

    else:
        # return request.method
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
