from django.urls import path
from . import views

app_name='electroapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('checkout/',views.checkout,name='checkout'),
    # path('add/',views.add_movie,name='add_movie'),
    # path('update/<int:id>/',views.update,name='update'),
    # path('delete/<int:id>/',views.delete,name='delete')
]