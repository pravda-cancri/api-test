import json
from logg import log
v="usernames/users.json"
def _save():
    with open(v, 'w') as f:
        json.dump(notes, f)
def _open():
    global notes
    try:
        with open(v) as f:
            notes = json.load(f)
    except:
        print("Could not load users.json")
        notes = {}
_open()
from flask import Blueprint,request
user = Blueprint('user', __name__)

@user.route('/api/user/<uuid>', methods=['GET'])
def run(uuid):
    log(request.access_route[0],"GET",uuid)
    _open()
    args = request.args
    time = args.get('time')
    online = args.get('online')
    login = args.get('login')
    if login=="true":
        if uuid in notes:
            send="true"
            notes[uuid]=int(time),online
        else:
            send="false"
    else:
        notes[uuid]=int(time),online
    _save()
    return send

@user.route('/api/get', methods=['GET'])
def done():
    _open()
    args = request.args
    user = args.get('user')
    time = args.get('time')
    online = args.get('online')
    send=""
    if user in notes:
        if time=="true" and online=="true":
            print("ddw")
            send={user:notes[user]}
        elif online=="true":
            send={user:notes[user][1]}
        elif time=="true":
            send={user:notes[user][0]}
        else:
            send = "not existant"
    else:
        send="not existant"
    return send