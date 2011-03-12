from fabric.api import run, cd


def update():
    with cd ('/usr/local/src/obudget'):
        run ('git pull')
        run ('bin/buildout')
        run ('bin/django syncdb --migrate')
        return run('bin/test')

def refresh():
    run('kill -HUP `cat /var/run/gunicorn/obudget.pid`')

