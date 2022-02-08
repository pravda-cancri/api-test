

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return '<h1>This is the api storage section!</h1>'


from games.game import game
from users import user
app.register_blueprint(game)
app.register_blueprint(user)
app.run(host='0.0.0.0', port=8080)