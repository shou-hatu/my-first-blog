from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
]


"""post_list という名前の ビュー をルートURLに割り当てている"""
"""name='post_list' は、ビューを識別するために使われるURL の名前"""
