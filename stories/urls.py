from crypt import methods
from unicodedata import name
from django.urls import path
from .views import Index, contact, strories, single, Test
from django.views.generic import TemplateView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('strories/', strories, name='strories'),
    path('single/<slug:slug>/', single, name='single'),
    # path('ornek/', TemplateView.as_view(template_name='test.html'), name='test'),
    path('ornek/', Test.as_view(), name='test')
]