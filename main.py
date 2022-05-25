from flask import Flask, request,render_template
from logg import log
app = Flask(__name__,template_folder='template')

@app.route('/')
def hello_world():
  return render_template('index.html')
    
@app.before_request
def before_request_callback(): 
    method=request.method
    args = request.args
    log(request.access_route[0],method,*[i for i in args.listvalues() if "true" not in i])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
from swoa.swo import swo
from users import user
from readlog import logs
from images.image import images
from video.videos import videos
app.register_blueprint(videos)
#app.register_blueprint(user)
app.register_blueprint(swo)
app.register_blueprint(logs)
app.register_blueprint(images)
app.register_error_handler(404, page_not_found)
app.run(host='0.0.0.0', port=8080)