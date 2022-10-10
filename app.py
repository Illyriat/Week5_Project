from flask import Flask, render_template

from controllers.products_controller import *
from controllers.type_controller import *
from controllers.manufacture_controller import *

# from controllers. import tasks_blueprint

app = Flask(__name__)

app.register_blueprint()

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)