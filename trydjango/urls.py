from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, about_view, contact_view

urlpatterns = [
    # products
    path('products/', include('products.urls')),

    #blog
    path('blog/', include('blog.urls')),

    # pages
    path('about/', about_view),
    path('contact/', contact_view),
    path('home/', home_view),

    # django
    path('admin/', admin.site.urls),
]
