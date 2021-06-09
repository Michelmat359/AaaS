from setuptools import setup, find_packages

setup(name='AaaS',
    description='Algorithm as a Service',
    author='Miguel A. Mateo-Casali',
    url='',
    package_dir={'': 'src'}, 
    packages=find_packages('src'),
    install_requires=[
        'connexion[swagger-ui]',
        'flask-cors',
        'flask_pymongo',
        'redis',
    ],
)
