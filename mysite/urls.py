"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

# urlpatterns는 웹사이트 주소 뒤에 붙는 index를 붙일 수 있도록 관리
# 현재 polls/ 와 admin/ 이 있으므로, 웹사이트 주소 뒤에 8000/polls/ 라고 붙이면 접근가능
urlpatterns = [
    # url을 최상단 urlconf에서도 볼 수 있도록 urlpatterns에 추가
    path("polls/", include("polls.urls")),
    path('admin/', admin.site.urls),
]
