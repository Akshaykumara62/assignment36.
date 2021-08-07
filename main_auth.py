from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1/Ravana'
app.config['SECRET_KEY'] = "random string"

github_blueprint = make_github_blueprint(client_id = '1f6e000e8e5ccec53db2',client_secret ='c04abfba367ff8f771b6cd497d00a9313af62f64
')

app.register_blueprint(github_blueprint,url_prefix ='/github_login')

@app.route("/github")
def github_login():
	if not github.authroized:
		return redirect(url_for('github.login'))
	account_info = github.get('/user')
	
	if account_info.ok:
		
	return <h1>Request</h1>

if __name__=='__main__';
	app.run(host ='0.0.0.0', post= 8080, debug=True)