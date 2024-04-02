class TestConfig(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://cat_user:1234@localhost:5432/test_cat_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_PATH = 'public/image/cats'
    TESTING = True