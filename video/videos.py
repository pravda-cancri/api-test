import os,json
    
def _save(v, notes):
    with open(v, 'w') as f:
        json.dump(notes, f)


def _open(v):
    global notes

    with open(v) as f:
        notes = json.load(f)


    return notes
from flask import Blueprint, request, render_template

videos = Blueprint('videos', __name__)
@videos.route('/videointer/<uuid>/<video>')
def get_file(uuid,video):
    print("video/" + uuid+"/store.json")
    print(uuid)
    notes = _open("video/" + uuid+"/store.json")
    print(notes)
    
    if video in notes:
        print(notes[video])
        return render_template('video.html',var1name=notes[video])
    
