from system.core.controller import *

class Users(Controller):
  def __init__(self, action):
    super(Users, self).__init__(action)
    self.load_model('User')
    self.db = self._app.db

  def index(self):
    pass

  def friendship(self, id):
    friends = self.models['User'].getFriends(id)
    notfriends = self.models['User'].getNotFriends(id)
    print "NOTFrIEND: {}".format(notfriends)
    return self.load_view('users/user.html', friends=friends, notfriends=notfriends)

  def notfriends(self, id):
    notfriends = self.models['User'].getNotFriends(id)
    print "NOTFrIEND: {}".format(notfriends)
    return self.load_view('users/user.html', friends=notfriends)

  def new(self):
    return self.load_view('products/add.html')

  def addProduct(self):
    productData = {
      'name': request.form['name'],
      'description': request.form['description'],
      'price': request.form['price']
    }

    self.models['Product'].addProduct(productData)
    return redirect('/products/display')

  def displayUserView(self, email):
    user = self.models['User'].getUserByEmail(email)[0]
    print "USERDISPLAY: {}".format(user)
    return self.load_view('users/display_user.html', user=user)

  def update(self, productId):
    product = {}
    product['name'] = request.form['name']
    product['description'] = request.form['description']
    product['price'] = request.form['price']
    product = self.models['Product'].updateProductById(product, productId)
    return redirect('/products/display')

  def delete(self, productId):
    product = self.models['Product'].deleteProductById(productId)
    return redirect('/products/display')

  def show(self, email):
    return self.displayUserView(email)

  def doAction(self, email):
    print "FRIEND email: {}".format(email)
    action = request.form['action']
    if (action == 'View Profile'):
      return self.displayUserView(email)

    if (action == 'Add as  Friend'):
      pass
      #return self.displayUserView(email)

    if (action == 'Remove as Friend'):
      return self.delete(email)

