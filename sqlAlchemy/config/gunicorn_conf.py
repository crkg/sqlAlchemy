import multiprocessing
import getpass

base_dir = f'/Users/{getpass.getuser()}/PycharmProjects/'
gunicorn_dir = base_dir + 'gunicorn/'

#server
bind = '0.0.0.0:8443'
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 2000
daemon = True
#certfile = base_dir + 'ssl_keys/<application name>.pem'
#keyfile = base_dir + 'ssl_keys/<application_name>.key'

errorlog = gunicorn_dir + '/var/log/error.log'
asseslog = gunicorn_dir + '/var/log/access.log'

