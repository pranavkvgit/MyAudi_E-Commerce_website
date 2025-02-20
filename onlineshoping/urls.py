"""
URL configuration for onlineshoping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
import app2.views
from django.conf.urls.static import static
from onlineshoping import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app2.views.Home_pge,name='Home'),
    path('Login_page2/',app2.views.Login_Pge,name='Login_page2'),
    path('Registration_Form/',app2.views.Register_pge,name='Registration_Form'),
    path('user_page/',app2.views.user_pge,name='user_page'),
    path('admin_page/',app2.views.admin_pge,name='admin_page'),
    path('product_page/',app2.views.product_pge,name='product_page'),
    path('product_view_page/',app2.views.viewproduct,name='product_view_page'),
    
    path('product_details/<sid>',app2.views.product_details,name='product_details'),

    path("add-to-cart/", app2.views.add_to_cart, name="add_to_cart"),
    path("cart_page/", app2.views.cart_page, name="cart_page"),
    
    path("remove_item/<id>", app2.views.remove_item, name="remove_item"),
    
    path("order_list/", app2.views.order_list, name="order_list"),
    path("delete_order/<int:order_child_id>", app2.views.delete_order, name="delete_order"),
   


    

]+ static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
