"""
Definition of urls for fbBirthdayMessager.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

urlpatterns = [
    url(r'^$', app.views.home, name='Index')
    
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]

