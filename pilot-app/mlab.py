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

# mongodb://admin:admin@ds021182.mlab.com:21182/c4e

host2 = 'ds021182.mlab.com'
port2 = 21182
db_name2 = 'c4e'
user_name2 = 'admin'
password2 = 'admin'

def connect2():
    mongoengine.connect(
        db_name2,
        host=host2,
        port=port2,
        username=user_name2,
        password=password2
    )

