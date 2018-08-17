from flask import Flask, render_template
app = Flask(__name__) # tao ra server gan vao app


@app.route('/') # / nay nghia la vao trang chu, vao route thi chay function ben duoi va nhung gi function nay return
def index():
   
    posts = [
        {"title": "Thơ con ếch",
        "content": "Nội dung bài thơ",
        "author": "Tommy Le",
        "author_sex": 1},
        {"title": "Thơ con ếch",
        "content": "Nội dung bài thơ",
        "author": "Thu Minh",
        "author_sex": 0},
        {"title": "Thơ con ếch",
        "content": "Nội dung bài thơ",
        "author": "Tommy Le",
        "author_sex": 1},
        {"title": "Thơ con ếch",
        "content": "Nội dung bài thơ",
        "author": "Thu Minh",
        "author_sex": 0},
    ]

    return render_template('index.html',
                                posts=posts
                                    )
    
@app.route('/hello') # route phai la duy nhat va function tuong ung cung phai duy nhat
def say_hello():
    return "Hello there"

@app.route('/say-hi/<name>/<age>')
def say_hi(name, age):
    return "Hi {}, you're {} years old".format(name, age)

@app.route('/sum/<int:x>/<int:y>')
def calc(x, y):
    return str(x + y)

if __name__ == '__main__': # kiem tra xem file app nay co chay truc tiep hay khong
  app.run(debug=True) #debug = True thi server chay lai luon neu co thay doi con khong de thi phai restart lai server
 