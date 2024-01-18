#Replace 'your-db-name', 'your-db-host', your-db-port, 'your-db-username', and 'your-db-password' with your actual MongoDB database name, host, port, username, and password.
#Now, you can use Django's ORM with MongoDB as if it were a SQL database. You don't need to write any MongoDB specific code. All your models.py files remain the same.
#Please note that you need to have MongoDB installed and running in your workspace. If it's running on a different server, replace the 'your-db-host' and your-db-port with the correct host and port. If you're using MongoDB Atlas, the host would be the MongoDB connection string.
#If you're using MongoDB Atlas, you can use the following settings.py file:


DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'your-db-name',
        'CLIENT': {
            'host': 'your-db-host',
            'port': your-db-port,
            'username': 'your-db-username',
            'password': 'your-db-password',
            'authMechanism': 'SCRAM-SHA-1',
        }
    }
}