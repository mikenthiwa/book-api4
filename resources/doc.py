from flask import Blueprint
from flask_restplus import Api


doc_api = Blueprint('resources.doc', __name__)
api = Api(doc_api, doc='/documentation')