import Table

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/', include('Table.urls'))
]

handler404 = Table.views.handler_404
