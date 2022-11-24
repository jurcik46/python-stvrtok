from flask import Blueprint, render_template, request, jsonify
from models import users_model
from helpers import jwt_helper
entrance_blueprint = Blueprint('entrance', __name__)

@entrance_blueprint.route('/login',methods=['POST'])   
def login_user():
    user_data = request.json
    user_model = users_model.get_user_by_email(user_data['email'])
    if user_model == None:
        return jsonify({"msg": "User not found!!!"}), 404
    if not users_model.compare_user_password(user_model, user_data['password']):
        return jsonify({"msg": "User password is incorrect"}), 403
    jwt_token=""
    try:
        jwt_token = jwt_helper.encode_auth_token(user_model["password"])
    except Exception as ex:
        return jsonify({"msg": "User JWT failed", "exception": ex}), 500
    del user_model["password"]
    print(jwt_token)
    result = {
        "user": user_model,
        "jwt": jwt_token
    }
    return jsonify(result), 200



#localhost/api/v1/entrance/registration
@entrance_blueprint.route('/registration',methods=['POST'])   
def registration():
    user_data= request.json
    if 'username' not in user_data or user_data['username'] is None or user_data['username'] is "":
        return jsonify({"msg":"User is required!!!"}), 400        
    return jsonify(users_model.create_user(user_data['username'],user_data['password'], user_data['email'])),200
    
    
    
#localhost/api/v1/entrance/all-users   
@entrance_blueprint.route('/all-users',methods=['GET'])   
def get_all_users():
    return jsonify(users_model.get_all_user()), 200   
