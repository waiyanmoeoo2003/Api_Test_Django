from django.urls import path

from . import views

app_name = "api"

urlpatterns = [
    path('challenges/list',views.get_challenges,name='challenges_list'),
    path('challenges/<int:id>',views.get_challenge_by_id,name='get_challenge_by_id')
]