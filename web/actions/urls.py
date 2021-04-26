from django.urls import path
from .views import (
    ActionListView,
    ActionUpdateView,
    ActionDetailView,
    ActionDeleteView,
    ActionCreateView,
    ActionPendingConfirmationListView,
)

urlpatterns = [
    path('<int:pk>/edit/',
         ActionUpdateView.as_view(), name='action_edit'),
    path('<int:pk>/',
         ActionDetailView.as_view(), name='action_detail'),
    path('<int:pk>/delete/',
         ActionDeleteView.as_view(), name='action_delete'),
    path('new/', ActionCreateView.as_view(), name='action_new'),
    path('pending/', ActionPendingConfirmationListView.as_view(), name='action_pending'),
    path('', ActionListView.as_view(), name='action_list'),
]
