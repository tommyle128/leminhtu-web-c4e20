from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/about-me')
def about_me():
    info = {
        "name": "Tommy Le",
        "age": 30,
        "hobbies": "gym and music",
        "work": "cofounder of a startup"
    }
    return render_template("about_me.html", info=info)

@app.route('/school')
def techkids():
    return redirect("https://techkids.vn/")

if __name__ == '__main__': 
  app.run(debug=True) 
 