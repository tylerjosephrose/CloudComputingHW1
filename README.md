# CloudComputingHW1
## Documentation for running django with nginx and uwsgi on CentOS 7
1. Install Python 3.6 with `yum install python36`
2. Install nginx with `yum install nginx`
3. Install the latest version of Django with `python36 -m pip install django`
4. Install uwsgi for Python with `python36 -m pip install uwsgi`
5. Create an nginx config file for your app in `/etc/nginx/conf.d/<filename>.conf`
6. Contents of the nginx config file should be similar to the following:
```bash
upstream django {
    server unix:///path/to/your/socket/<name>.sock;
    #server 127.0.0.1:8001;
}

# server configuration
server {
    listen      80;

    server_name <IP of system>;
    charset     utf-8;

    client_max_body_size        75M;

    location /static {
        alias /path/to/django/static/files/static;
    }

    location / {
        uwsgi_pass      django;
        include         /etc/nginx/uwsgi_params;
    }
}
```
7. Create a uwsgi configuration file for your app which should have contents similar to the following:
```bash
[uwsgi]

# Django settings
chdir           =/path/to/django/project
module          = <ProjectName>.wsgi

# Process settings
master          = true
processes       = 10
socket          = /path/to/your/socket/<name>.sock
chmod-socket    = 666
vacuum          = true
```
8. Start nginx with `service nginx start`
9. Start uwsgi with `uwsgi --ini </path/to/uwsgi/config/file.ini`
10. Now you should be good to start up with your Django app!
