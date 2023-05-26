from jogoteca import app
import os

SECRET_KEY = 'trovador'
SQLALCHEMY_DATABASE_URI = \
    "{SGBD}://{username}:{password}@{local_port}/{database}".format(
        SGBD = 'mysql+mysqlconnector',
        username = 'root',
        password = 'Tsubasa12',
        local_port = 'localhost',
        database = 'jogoteca'
)

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/upload'
