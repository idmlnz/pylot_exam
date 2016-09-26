from system.core.model import Model

class User(Model):
    def __init__(self):
        super(User, self).__init__()

    def getFriends(self, loginId):
        query = "SELECT u1.firstname, u1.lastname, u2.firstname AS friend_firstname, u2.lastname AS friend_lastname,  u2.email AS friend_email FROM users AS u1, users AS u2, friendship AS f WHERE u1.id = f.user_id AND u2.id = f.friend_id AND u1.id={}".format(loginId)
        return self.db.query_db(query)

    def getNotFriends(self, loginId):
        query="select * from users where users.id not in ( SELECT u2.id FROM users AS u1, users AS u2, friendship AS f WHERE u1.id = f.user_id AND u2.id = f.friend_id AND u1.id={})".format(loginId) ;

        print "QUERY NOT : {}" .format(query)
        #self.db.query_db(query)
        #query = "select users.id from users where users.id not in( SELECT u1.firstname, u1.lastname, u2.firstname AS friend_firstname, u2.lastname AS friend_lastname,  u2.email AS friend_email FROM users AS u1, users AS u2, friendship AS f WHERE u1.id = f.user_id AND u2.id = f.friend_id AND u1.id={})".format(loginId)

        return self.db.query_db(query)


    def getUserByEmail(self, email):
        query = "SELECT * from users where email=\"{}\"".format(email)
        print "BY EMAIL: {}.format(query)\n"
        return self.db.query_db(query)

    def updateProductById(self, product, productId):
        query = "UPDATE product SET name = :name, description = :description, price = :price, updated_at=NOW() "\
          "WHERE id = {}".format(productId)
        data = {
            'name': product['name'],
            'description': product['description'],
            'price': product['price']
        }
        return self.db.query_db(query, data)

    def addProduct(self, product):
        query = "INSERT into product (name, description, price, created_at, updated_at ) values (:name, :description, :price, NOW(), NOW())"
        data = {
            'name': product['name'],
            'description': product['description'],
            'price': product['price'],
        }
        return self.db.query_db(query, data)

    def deleteProductById(self, productId):
        query = "DELETE FROM product WHERE id = {}".format(productId)
        return self.db.query_db(query)
