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

routes['GET']['/registers/new'] = 'Registers#new'
routes['POST']['/registers/add'] = 'Registers#add'
routes['POST']['/registers/login'] = 'Registers#login'
