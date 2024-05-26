from django.urls import path

from . import views

# path의 인자 4가지
# 첫번째(route) : URL pattern
# 두번째(view) : view
urlpatterns = [
    path("", views.index, name="index"),
]
