from redis import StrictRedis

class Config(object):
    SQLALCHEMY_DATABASE_URI ="mysql+pymysql://root:@127.0.0.1:3306/information27"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "w/YHy55xaBzqquY/7IccwsDkKFedltkasyDhSVqbRWeDdzAD1Jzm+clB3iGK+Czh"
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    DEBUG = True
    SESSION_TYPE = "redis"
    SESSION_USE_SIGNER = True
    #设置是否过期
    SESSION_PERMANENT = False
    #设置session过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2
    #制定SESSION保存到REDIS
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)

class DevelelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True


config={
    "Develop" : DevelelopmentConfig,
    "Testing" : TestingConfig,
    "PRODUCTION" : ProductionConfig
}