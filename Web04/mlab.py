import mongoengine

# mongodb://admin3:admin123@ds233228.mlab.com:33228/video-listing-site

host = "ds233228.mlab.com:33228"
port = 33228
db_name = "video-listing-site"
user_name = "admin3"
password = "admin123"


def connect():
    mongoengine.connect(
        db_name,
        host=host,
        port=port,
        username=user_name,
        password=password)



