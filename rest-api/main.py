from flask import Flask, render_template, request, jsonify
import configs.main_config
from controllers import entrace_controller, users_controller, user_controller
from middlewares import auth, is_admin
app_config = configs.main_config.APP_CONFIG
app = Flask(__name__, template_folder=app_config.get("template_folder"))

app.register_blueprint(entrace_controller.entrance_blueprint, url_prefix=f"{app_config.get('api_prefix')}/{app_config.get('api_version')}/entrance")
app.register_blueprint(users_controller.blueprint, url_prefix=f"{app_config.get('api_prefix')}/{app_config.get('api_version')}/users")
app.register_blueprint(user_controller.blueprint, url_prefix=f"{app_config.get('api_prefix')}/{app_config.get('api_version')}/user")


app.before_request_funcs = {
    users_controller.controller_name : [auth.is_auth, is_admin.is_admin],
    user_controller.controller_name : [auth.is_auth]
}


@app.route('/score',  methods=['GET'])
def score():
    score_input = int(request.args.get('score', 0))
    result = {"msg":"Success", "youre_score": score_input}
    if score_input < 5:
        result['msg'] = "Failed!!"
        return jsonify(result), 406
        
    return jsonify(result), 200
        

if __name__ == '__main__':
    app.run(app_config.get("host"), app_config.get("port"), app_config.get("debug"))