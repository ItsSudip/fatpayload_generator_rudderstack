# fatpayload_generator_rudderstack
This repo can be used to create fat payload randomly. You can give schema of the payload, writekey, size of the users to be created randomly.
Clone this repository in a directory and run the following commands
1. Sudo apt-get install virtualenv 
2. virtualenv venv
3. venv/bin/activate
4. pip install Flask
5. pip3 install requests
6. python3 app.py

Then open "localhost:5000" in browser.
(Before submitting run rudder-server and rudder-transformer locally.)

![alt text](https://github.com/ItsSudip/fatpayload_generator_rudderstack/blob/main/assets/Screenshot%202021-07-09%20at%204.22.10%20PM.png?raw=true)

I have created the testing for track call with <b>"userListDelete"</b> and <b>"userListAdd"</b> in properties for <b>facebook custom audience</b> only. <br/>
So for a successfull call with random users you have to provide the following payload:
## userListAdd:
```javascript
{
    "userId": "user123",
    "event": "Product Purchased",
    "properties": {
        "name": "Rubik's Cube",
        "revenue": 4.99,
        "userListAdd": [
        ]
    },
    "context": {
        "ip": "14.5.67.21"
    },
    "timestamp": "2020-02-02T00:23:09.544Z"
}
```
## userListDelete:
```javascript
{
    "userId": "user123",
    "event": "Product Purchased",
    "properties": {
        "name": "Rubik's Cube",
        "revenue": 4.99,
        "userListDelete": [
        ]
    },
    "context": {
        "ip": "14.5.67.21"
    },
    "timestamp": "2020-02-02T00:23:09.544Z"
}
```
<h3>After a successfull submission the result will be something like that:</h3>

![alt text](https://github.com/ItsSudip/fatpayload_generator_rudderstack/blob/main/assets/Screenshot%202021-07-15%20at%2011.32.51%20AM.png?raw=true)

