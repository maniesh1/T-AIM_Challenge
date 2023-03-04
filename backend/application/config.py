import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    WTF_CSRF_ENABLED = False
    # SECURITY_TOKEN_AUTHENTICATION_HEADER = "Authentication-Token"



class LocalDevelopmentConfig(Config):
    SQLITE_DB_DIR = os.path.join(basedir, "../db_directory")
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "db.sqlite3")
    DEBUG = True
    SECRET_KEY = "vjksiut78hJKfilu"



