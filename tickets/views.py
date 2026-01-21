from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Ticket
from .serializers import TicketSerializer
from .permissions import (
    CanCreateTicket,
    CanViewTicket,
    CanAssignTicket,
    CanChangeStatus
)

#endpoints
from rest_framework.views import APIView
from users.permissions import IsAdmin
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

class TicketListCreateView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, CanCreateTicket]

    def get_queryset(self):
        user = self.request.user

        if user.is_admin_role:
            return Ticket.objects.all()

        if user.is_resolver:
            return Ticket.objects.filter(assigned_to=user)

        return Ticket.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated, CanViewTicket]

class TicketAssignView(APIView):
    permission_classes = [IsAuthenticated, CanAssignTicket]

    def patch(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        ticket.assigned_to_id = request.data.get('user_id')
        ticket.save()
        return Response({'assigned': True})
    
class TicketStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated, CanChangeStatus]

    def patch(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        ticket.status = request.data.get('status')
        ticket.save()
        return Response({'status': 'updated'})
