from flask import Blueprint, render_template, request, jsonify
from helpers import jwt_helper


def is_auth():
    try:
        print("is_auth")
        # print(request.headers.get('Authorization'))
        # print(request.headers.get('Authorization')[7:])
        jwt_token = request.headers.get('Authorization')[7:]
        payload = jwt_helper.decode_auth_token(jwt_token)
        request.user = payload['sub']
    except Exception as e:
        print(e)
        return jsonify({ "msg": "Authorization failed!!"}), 401