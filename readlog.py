import json


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


def timesused(x, v):
    command = x
    if command in notes:
        notes[command] = notes[command] + 1
        _save(v, notes)
    elif command not in notes:
        notes[command] = 1
        _save(v, notes)


class save():
    def __init__(self, ip, type, time, args):
        self.ip: int = ip
        self.type: int = type
        self.time: int = time
        self.args: int = args


def lol():
    g = open("log.txt", "r")
    g = g.read().splitlines()
    f = []
    for x in g:
        _ = x.strip().split("#")
        f.append(save(_[0], _[1], _[2], _[3]))
    for x in f:
        _open("ips.json")
        #print(x.ip)
        timesused(x.ip, "ips.json")
    for x in f:
        _open("types.json")
        #print(x.type)
        timesused(x.type, "types.json")
    for x in f:
        _open("files.json")
        for p in eval(x.args):
            if p[0] != "":
                timesused(p[0], "files.json")



from flask import request, Blueprint, render_template

logs = Blueprint('logs', __name__)


@logs.route('/api/update', methods=['GET'])
def runs():
    args = request.args
    update = args.get('what')
    if update == "log":
        lol()
        g = open("log.txt", "w")
        g.write("")
        g.close()
    v1n = "files conected to"
    _open("files.json")
    v1 = ""
    for x in notes:
        v1 += x + " : " + str(notes[x]) + " \n "
    v2n = "ip addressess connected"
    _open("ips.json")
    v2 = ""
    for x in notes:
        v2 += x + " : " + str(notes[x]) + " \n "
    v3n = "type of request"
    _open("types.json")
    v3 = ""
    for x in notes:
        v3 += x + " : " + str(notes[x]) + " \n "
    return render_template('stats.html',
                           var1=v1,
                           var2=v2,
                           var3=v3,
                           var1name=v1n,
                           var2name=v2n,
                           var3name=v3n)
