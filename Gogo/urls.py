
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from registration import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Testimonials.urls')),
    path('api/', include('booking_summary.urls')),
    path('api/client/login/', views.ClientLogin),
    path('api/driver/login/', views.DriverLogin),
    path('api/client-register/', views.ClientRegister),
    path('api/driver-register/', views.DriverRegister),
    path('api/auth/', views.test_token),
    path('docs/', include_docs_urls(title = 'GogoApi')),
    path('schema', get_schema_view(
        title="Gogo",
        description="Api for Gogo",
        version="1.0.0"
    ), name='openapi-schema'),
]
