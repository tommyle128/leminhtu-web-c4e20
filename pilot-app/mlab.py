import mongoengine

# mongodb://admin2:Tommy999@ds123822.mlab.com:23822/muadongkhonglanh-c4e20

host = "ds123822.mlab.com"
port = 23822
db_name = "muadongkhonglanh-c4e20"
user_name = "admin2"
password = "Tommy999"


def connect():
    mongoengine.connect(
        db_name,
        host=host,
        port=port,
        username=user_name,
        password=password)

