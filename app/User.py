from flask import Flask, render_template, request
import json
import sqlite3
import db.DBUtil as dbUtil


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/showSignUp")
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp', methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']

    # sql = 'SELECT USER_NAME, PASSWORD FROM USER WHERE USER_NAME = ? AND PASSWORD = ?'
    # param = [_name, _password]
    print("Input Value :: {} {} {}".format(_name, _email, _password))
    sqlite = dbUtil.sqlite("D:/sqlite3/deploy")

    sql1 = "INSERT INTO USER (USER_NAME, PASSWORD, EMAIL) VALUES('{}', '{}', '{}')"
    params =[_name, _password, _email]
    ret = sqlite.insert(sql1, params)


    sql2 = "SELECT USER_NAME, PASSWORD, EMAIL FROM USER WHERE 1 = 1"
    user = sqlite.select(sql2, params)
    jsonUser = json.dumps(user)

    print("User :: {}".format(jsonUser))
    if _name and _email and _password:
        return json.dumps({
            'html' : '<span>All fields good!</span>'})
    else:
        return json.dumps({
            'htm;' : '<span> Enter the required fields </span>'
        })

if __name__ == '__main__':
    app.run(port=8080, debug=True)
