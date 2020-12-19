"""pizzashopproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url,include
from pizzashopapp import views,apis
from django.contrib.auth.views import LoginView, LogoutView

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^pizzashop/sign_in/$', LoginView.as_view(template_name='pizzashop/sign_in.html'), name='sign-in'),
    url(r'^pizzashop/sign_out/$', LogoutView.as_view(next_page='/'), name='sign-out'),
    url(r'^pizzashop/$', views.pizzashop_home, name='pizzashop-home'),
    url(r'^pizzashop/sign_up', views.pizzashop_sign_up, name='pizzashop-sign-up'),
    url(r'^pizzashop/account/$', views.pizzashop_account,name='pizzashop-account'),
    url(r'^pizzashop/pizza/$', views.pizzashop_pizza,name='pizzashop-pizza'),
    url(r'^pizzashop/pizza/add/$', views.pizzashop_add_pizza, name='pizzashop-add-pizza'),
    url(r'^pizzashop/pizza/edit/(?P<pizza_id>\d+)/$', views.pizzashop_edit_pizza, name='pizzashop-edit-pizza'),
    #url(r'^pizzashop/client_role/$', views.test_model, name='pizzashop-clent-role'),
    url(r'^pizzashop/client_role/(?P<user_id>\d+)/$', views.test_model_2, name='pizzashop-clent-role'),
    #APIS
    url(r'^api/client/pizzashops/$', apis.client_get_pizzashops),
    url(r'^api/client/pizzas/(?P<pizzashop_id>\d+)/$', apis.client_get_pizzas),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
