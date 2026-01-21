from django.urls import path
from .views import (
    TicketListCreateView,
    TicketDetailView,
    TicketStatusUpdateView,
    TicketAssignView
)

urlpatterns = [
    path('', TicketListCreateView.as_view()),
    path('<int:pk>/', TicketDetailView.as_view()),
    path('<int:pk>/status/', TicketStatusUpdateView.as_view()),
    path('<int:pk>/assign/', TicketAssignView.as_view()),
]
