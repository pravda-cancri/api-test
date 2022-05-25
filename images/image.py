import os.path
from flask import request, Blueprint, send_file
from werkzeug.utils import secure_filename

images = Blueprint('images', __name__)

@images.route('/api/images', methods=['GET'])
def get_image():
    args = request.args
    file = args.get('file')
    path = "images/" + file
    if os.path.exists(path):
        filename = path
    else:
        filename = "images/errorinv.png"
    return send_file(filename, mimetype='image/png')

@images.route('/api/upload/image/<uuid>', methods=['POST'])
def get_images(uuid):
    args = request.args
    name = args.get('name')
    filename = secure_filename(name)
    path = "images/"+uuid+"/"+filename
    try:
        os.mkdir("images/"+uuid)
    except:
        pass
    w=open(path,"wb")
    w.write(request.data)
    w.close()
    return {}
