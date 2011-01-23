from setuptools import setup, find_packages

install_requires = [
    'South',
    'django-piston',
    'django-extensions',
    'python-memcached',
    'gunicorn',
    'psycopg2',
    ]
setup(
        name = "obudget",
        version = "0.1",
        url = 'http://github.com/hasadna/obudget',
        description = "Bringing transperancy to the Israeli Knesset",
        author = 'Benny Daon, Imri Goldberg and others',
        packages = find_packages('src'),
        package_dir = {'': 'src'},
        install_requires = install_requires,
        classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'License :: OSI Approved :: BSD License',
                 'Natural Language :: Hebrew',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Programming Language :: JavaScript'],
)


