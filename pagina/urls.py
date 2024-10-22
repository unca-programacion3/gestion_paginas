from django.urls import path
from . import views


app_name = 'pagina'
urlpatterns = [
    path('', views.lista_paginas, name='lista_paginas'),
    path('crear/', views.crear_pagina, name='crear_pagina'),
    path('editar/<int:pk>/', views.editar_pagina, name='editar_pagina'),
]
