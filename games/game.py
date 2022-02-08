import json
v="games/game.json"
def _save():
    with open(v, 'w') as f:
        json.dump(notes, f)
def _open():
    global notes
    try:
        with open(v) as f:
            notes = json.load(f)
    except FileNotFoundError:
        print("Could not load vend.json")
        notes = {}
_open()

from flask import Blueprint,request
game = Blueprint('game', __name__)
@game.route('/game', methods=['GET'])
def search():
    _open()
    args = request.args
    name = args.get('name')
    score = args.get('score')
    update = args.get('update')
    if update == "true" and not score==None:
        if name not in notes:
            notes[name] =int(score)
            result="done"
        else:
            notes[name] +=int(score)
            result="done"
    else:
        if name in notes:
            print()
            result = {key: value for key, value in notes.items() if key == name}
        else:
            result="done"
    _save()
    return result