# django_custom_authentication
The repo illustrates how django custom authentication can be created along with multiple user-types

# create a virtual-environment
~pip freeze <br />
~mkvirtualenv django-custom-authentication

# install requirements.txt
pip install -r requirements.txt

# check multiple user models registration and login
For user (get and post) <br/>
http://127.0.0.1:8000/api/users/ <br/>

While registering user: <br/>

{ <br/>
    "email":"monir1@gmail.com", <br/>
    "username":"monir1" <br/>
}


For student (register) <br/>
http://127.0.0.1:8000/api/student/register/ <br/>

While registering: <br/>

{ <br/>
    "username":"student1@gmail.com", <br/>
    "password":"12345678" <br/>
}

For student (login) <br/>
http://127.0.0.1:8000/student/login/ <br/>

While loging in: <br/>
{ <br/>
    "username":"student1@gmail.com", <br/>
    "password":"12345678" <br/>
}


