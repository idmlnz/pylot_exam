from system.core.controller import *

class Registers(Controller):
  def __init__(self, action):
    super(Registers, self).__init__(action)
    self.load_model('Register')
    self.db = self._app.db

  def index(self):
    return self.load_view('registration/register.html')

  def new(self):
    return self.load_view('registration/register.html')

  def clearSession(self):
    session.clear()

  def add(self):
    userInfo = {}
    userInfo['firstname'] = request.form['firstname']
    userInfo['lastname'] = request.form['lastname']
    userInfo['email'] = request.form['email']
    userInfo['password'] = request.form['password']
    userInfo['confirm_password'] = request.form['confirm_password']
    userInfo['birthday'] = request.form['birthday']

    createStatus = self.models['Register'].createUser(userInfo)
    print "createstatus: {}".format(createStatus)
    if createStatus['status'] == True:
      session['users'] = createStatus['users']
      print "REGISTER session users: {}".format(session['users'])
    else:
      for message in createStatus['errors']:
        flash(message, 'regis_errors')
      return self.load_view('registration/register.html', error=createStatus['errors'], mesg_origin="register")

    return redirect("users/friendship/{}".format(createStatus['users']['id']))

  def home(self):
    return redirect("users/friendship/{}".format(session['users']['id']))

  def login(self):
    userInfo = {}
    userInfo['email'] = request.form['login-email']

    userInfo['password'] = request.form['login-password']
    loginStatus = self.models['Register'].checkUser(userInfo)

    if loginStatus['status'] == True:
      session['users'] = loginStatus['users']
      print "\nLOGIN session users: {}\n".format(session['users'])
    else:
      for message in loginStatus['errors']:
        flash(message, 'regis_errors')
      return self.load_view('registration/register.html', error=loginStatus['errors'], mesg_origin="login")

    print "\nXXX LOGIN session users: {}\n".format(session['users'])
    return redirect("users/friendship/{}".format(loginStatus['users']['id']))

  def logout(self):
    self.clearSession()
    print "\nSESSION is cleared on LOGOUT\n"
    return redirect('/')  # redirect to / FOR NOW
