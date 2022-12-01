from flask import Blueprint, render_template, request, jsonify
from helpers import jwt_helper


def is_admin():
    try:
        if request.user["role"] == "admin":
            return

    except Exception as e:
        print(e)
    return jsonify({ "msg": "Your are not allowed execude this endpoint. Only Admin!!"}), 401