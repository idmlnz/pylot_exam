from system.core.router import routes

"""
	  EXAM for pylot
    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""

routes['default_controller'] = 'Registers'

routes['GET']['/users/friendship/<id>'] = 'Users#friendship'
routes['GET']['/users/notfriends'] = 'Users#notfriends'
routes['POST']['/users/doAction/<email>'] = 'Users#doAction'




routes['GET']['/registers/home'] = 'Registers#home'
routes['GET']['/registers/new'] = 'Registers#new'
routes['GET']['/registers/clearsession'] = 'Registers#clearSession'
routes['POST']['/registers/add'] = 'Registers#add'
routes['POST']['/registers/login'] = 'Registers#login'
routes['GET']['/registers/logout'] = 'Registers#logout'
