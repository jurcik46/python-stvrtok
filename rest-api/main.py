from flask import Flask, render_template, request, jsonify
import configs.main_config
from controllers import entrace_controller
app_config = configs.main_config.APP_CONFIG
app = Flask(__name__, template_folder=app_config.get("template_folder"))

app.register_blueprint(entrace_controller.entrance_blueprint, url_prefix=f"{app_config.get('api_prefix')}/{app_config.get('api_version')}/entrance")



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