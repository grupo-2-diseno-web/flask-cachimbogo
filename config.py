class Config:
    SECRET_KEY = 'secret'
    BUNDLE_ERRORS = True
    JWT_SECRET_KEY = 'super-secret'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:asd123@cgo-db/cachimbogo'
    SQLALCHEMY_TRACK_MODIFICATIONS = False