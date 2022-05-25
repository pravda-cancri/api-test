import json
import time
from logg import log
    

    
def _save(v, notes):
    with open(v, 'w') as f:
        json.dump(notes, f)


def _open(v):
    global notes
    try:
        with open(v) as f:
            notes = json.load(f)
    except:
        print("Could not load users.json")
        notes = {}

    return notes



from flask import Blueprint, request

swo = Blueprint('swo', __name__)


@swo.route('/api/data/file', methods=['GET'])
def run():
    args = request.args
    at = args.get('file')
    #log(request.access_route[0],"GET",at)
    open("swoa/" + at, "a")
    if at.endswith(".json"):
        v = "swoa/"
        args = request.args
        file = args.get('update')
        get = args.get('get')
        v += at
        if get == "true":
            notes = _open(v)
            print(notes)
            return notes

        elif file != "":
            print(file)
            notes = eval(file)
            _save(v, notes)
            return {}
    elif at.endswith(".txt"):
        v = "swoa/"
        args = request.args
        file = args.get('update')
        get = args.get('get')
        v += at
        if get == "true":
            notes = open(v, "r")
            notes = notes.read()
            print(notes)
            return notes
        elif file != "":
            print(file)
            g = open(v, "w")
            g.write(file)
            g.close()
            return {}


@swo.route('/api/data/drop/files', methods=['POST'])
def run2():
    #log(request.access_route[0],"POST",at)
    args = request.args
    at = args.get('file')
    open("swoa/" + at, "a")
    if at.endswith(".json"):
        v = "swoa/"
        v += at
        file = request.json
        print(file)
        _save(v, file)
        return {}
    elif at.endswith(".txt"):
        v = "swoa/"
        v += at
        file = request.data
        print(file)
        g = open(v, "wb")
        g.write(file)
        g.close()
        return {}
