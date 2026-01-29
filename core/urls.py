from django.urls import path
from core import views

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('forum/', views.forum, name='forum'),
    path('business/', views.business, name='business'),
    path('base/', views.base, name='base'),
    path('magazine/', views.magazine, name='magazine'),
    path('market/', views.market, name='market'),
    path('wiki/', views.wiki, name='wiki'),
]