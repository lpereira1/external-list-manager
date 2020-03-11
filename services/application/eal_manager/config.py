import os
import yaml

class Config:
    file = os.getcwd() + '/eal_manager/conf/setup.yml'
    with open(file , 'r') as config:
        try: 
            configuration = yaml.load(config, Loader=yaml.FullLoader)
        except:
            print('Error Reading Yaml File')

    SECRET_KEY = configuration['setup']['forms_secret']
    SQLALCHEMY_DATABASE_URI = 'sqlite://' + configuration['setup']['database_location']
    MAIL_SERVER = configuration['setup']['mail_server']
    MAIL_PORT = configuration['setup']['mail_port']
    MAIL_USE_TLS = configuration['setup']['tls']
    MAIL_USERNAME = configuration['setup']['mail_user']
    MAIL_PASSWORD = configuration['setup']['mail_password']