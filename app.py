from flask import Flask
from flask_restplus import Api, Resource


flask_app = Flask(__name__)
app = Api(app = flask_app)

main_name_space = app.namespace('main', description='Main APIs')
no_mainname_space = app.namespace('no_main', description='No Main APIs')

@main_name_space.route("/")
class MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}


@no_mainname_space.route("/")
class No_MainClass(Resource):
	def get(self):
		return {
			"status": "Got new data"
		}
	def post(self):
		return {
			"status": "Posted new data"
		}		