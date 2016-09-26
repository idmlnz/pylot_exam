from flask.ext.bcrypt import Bcrypt
from system.core.model import Model
import re

class Register(Model):
    def __init__(self):
        super(Register, self).__init__()

    def checkUser(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid!')
        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 1:
            errors.append('Password must be at least 8 characters long')

        if errors:
            return {"status": False, "errors": errors}
        else:
            get_user_query = "SELECT * FROM users WHERE email=\"{}\"".format(info['email'])
            user = self.db.query_db(get_user_query)
            if user:
                if (info['password'] == user[0]['password']):
                    return {"status": True, "users": user[0]}
                else:
                    errors.append('Your email does not match your password!!')
                    return {"status": False, "errors": errors}
            else:
                errors.append('Your email does not exists.  Create one!!')
                return {"status": False, "errors": errors}

    def createUser(self, info):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # Some basic validation
        if not info['firstname']:
            errors.append('firstname cannot be blank')
        elif len(info['firstname']) < 2:
            errors.append('firstname must be at least 2 characters long')

        if not info['lastname']:
            errors.append('lastname cannot be blank')
        elif len(info['lastname']) < 2:
            errors.append('lastname must be at least 2 characters long')

        if not info['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(info['email']):
            errors.append('Email format must be valid [myemail@yahoo.com] !')

        if not info['password']:
            errors.append('Password cannot be blank')
        elif len(info['password']) < 1:
            errors.append('Password must be at least 8 characters long')

        elif info['password'] != info['confirm_password']:
            errors.append('Password and confirmation must match!')

        if errors:
            return {"status": False, "errors": errors}

        else:
            # add users to DB
            #pw_hash = bcrypt.generate_password_hash(info['password'])
            pw_hash = info['password']

            #check if users already exists
            get_user_query = "SELECT * FROM users where email=\"{}\"".format(info['email'])
            print "query: {}".format(get_user_query)
            try:
                user = self.db.query_db(get_user_query)
                print "users: {}".format(user)
                if user:
                    errors.append("{} already exists! Try login-in".format(info['email']))
                    return {"status": False, "errors": errors}
            except:
              pass

            insertQuery = "INSERT INTO users (firstname, lastname, email, password, birthday, created_at, updated_at) \
                VALUES (:firstname, :lastname, :email, :password, NOW(), NOW(), NOW())"

            userData = {
                'firstname': info['firstname'],
                'lastname': info['lastname'],
                'email': info['email'],
                'password': pw_hash
            }
            print "userdata: {}".format(userData)
            print "INSERT: {}\n".format(insertQuery)
            self.db.query_db(insertQuery, userData)

            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            user = self.db.query_db(get_user_query)
            return {"status": True, "users": user[0]}

