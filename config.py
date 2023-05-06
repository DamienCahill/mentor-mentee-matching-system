import os
config = {
    'host': os.environ.get('db_host', 'db'),
    'database': os.environ.get('db_name','mentor_mentee_matching_system'),
    'user': os.environ.get('db_username','root'),
    'password':os.environ.get('db_password','devpass')
}