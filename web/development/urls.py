from django.urls import path
from .views import (
    # DevelopmentCreateView,
    model_form_upload,
    DevelopmentDetailView,
    DevelopmentListView,
    DevelopmentUpdateView
)

urlpatterns = [
    path('create/', model_form_upload, name='development_create'),
    path('detail/<uuid:pk>/', DevelopmentDetailView.as_view(), name='development_detail'),
    path('update/<uuid:pk>/', DevelopmentUpdateView.as_view(), name='development_update'),
    path('', DevelopmentListView.as_view(), name='development_list'),
]
