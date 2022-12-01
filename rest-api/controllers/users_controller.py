
from flask import Blueprint, render_template, request, jsonify
from models import users_model
from helpers import jwt_helper

controller_name = 'users'
blueprint = Blueprint(controller_name, __name__)

#localhost/api/v1/users/   
@blueprint.route('/',methods=['GET'])   
def get_all_users():
    print("from controller")
    print(request.user["id"])
    print(request.user["email"])
    return jsonify(users_model.get_all_user()), 200   

@blueprint.route('/profile',methods=['GET'])
def get_profile():
    user_data = users_model.get_user_by_email(request.user["email"])
    return jsonify(user_data), 200   
