from flask import Flask, render_template
app = Flask(__name__)

users = {
    "tu":{
            "name": "Tu Le",
            "age": 30,
            "gender": "Male",
            "hobbies": "gym"
        },
    "tuan":{
            "name": "Tuan Le",
            "age": 36,
            "gender": "Male",
            "hobbies": "video games"
        }
    }

@app.route('/user/<username>')
def check_user(username):
    if username in users.keys():
        return render_template('user.html', info=users[username])
    else:
        return "User not found"

if __name__ == '__main__': 
  app.run(debug=True) 