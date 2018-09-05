from flask import *
import mlab
from mongoengine import *
from youtube_dl import YoutubeDL
from models.video import Video

app = Flask(__name__)
app.secret_key = "a super super secret key"

mlab.connect()

@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos=videos)

@app.route('/detail/<youtube_id>')
def detail(youtube_id):
    return render_template('detail.html', youtube_id=youtube_id)

@app.route('/admin/', methods=["GET", "POST"])
def admin():
    if "loggedin" in session:
        if session['loggedin'] == True:
            if request.method == "GET":
                videos = Video.objects()
                return render_template('admin.html',videos=videos)
            elif request.method == "POST":
                form = request.form
                link = form['link']
                
                ydl = YoutubeDL()

                data = ydl.extract_info(link, download=False)
                title = data['title']
                views = data['view_count']
                thumbnail = data['thumbnail']
                youtube_id = data['id']
                
                new_video = Video(
                    title=title,
                    views=views,
                    thumbnail=thumbnail,
                    youtube_id=youtube_id,
                    link=link
                )
                new_video.save()

                return redirect(url_for('admin'))
        else:
            return "Yêu cầu đăng nhập" 
        
    else:
        return "Yêu cầu đăng nhập"
@app.route('/login/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']
        
        #found_user = User.objects(username=username,
        #                            password=password)

        if username == "admin" and password == "admin":
            session['loggedin'] = True
            return redirect(url_for('admin'))
        else:
            return "Wrong username or password"

@app.route('/logout/')
def logout():
    session['loggedin'] = False
    return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)