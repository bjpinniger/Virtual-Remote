import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    CUCM = "ip_address" # enter ip address or fqdn of cucm
    VERSION = "12.0"
    CUCM_USER = os.environ.get("CUCM_USER")
    CUCM_PWD = os.environ.get("CUCM_PWD")
    FILTER = "%SX%"
    USERNAME = os.environ.get("TP_USERNAME")
    PASSWORD = os.environ.get("TP_PASSWORD")
    WTF_CSRF_ENABLED = True
    # Disable debugging
    DEBUG = True