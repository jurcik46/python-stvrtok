from flask import Flask, render_template, request
import configs.main_config
app_config = configs.main_config.APP_CONFIG
app = Flask(__name__, template_folder=app_config.get("template_folder"))

USERS= {}

@app.route('/', methods=['GET'])
def home():
    return render_template('/home/index.html',title="Flas title", body_text="asdasdas")

@app.route('/score',  methods=['GET'])
def score():
    score_input = int(request.args.get('score', 0))
    result = "Success"
    if score_input < 5:
        result = "Failed!!"
    return render_template('/score/score.html',score_template= score_input, result_template =result)


@app.route('/article/<int:article_id>',  methods=['GET'])
def articles(article_id):
    return render_template('/article/article.html',article_title= article_id)

@app.route('/registration', methods=['GET'])
def registration():
    return render_template('/registration/registration.html')
   
@app.route('/registration/user', methods=['POST'])
def registration_user():
    name = request.form.get('name')
    if name is None or name is "":
        return render_template('/registration/failed.html') 
    group1 = request.form.get('group1')
    if group1 is None:
        return render_template('/registration/failed.html') 
    USERS[name] = group1
    return render_template('/registration/succes.html') 
   
@app.route('/registration/users', methods=['GET'])
def registred_users():
    return render_template('/registration/registred_users.html',users= USERS ) 
   
if __name__ == '__main__':
    app.run(app_config.get("host"), app_config.get("port"), app_config.get("debug"))