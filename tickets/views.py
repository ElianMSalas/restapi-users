from rest_framework import generics, permissions
from .models import Ticket
from .serializers import TicketSerializer
from .permissions import IsOwnerOrAdmin

#imports endpoints
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Ticket
from users.permissions import IsAdmin


#ticket list
class TicketListCreateView(generics.ListCreateAPIView):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return Ticket.objects.all()
        return Ticket.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

#detail ticket
class TicketDetailView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

#change status
class TicketStatusUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def patch(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        ticket.status = request.data.get('status')
        ticket.save()
        return Response({'status': 'updated'})

#assign ticket owner
class TicketAssignView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def patch(self, request, pk):
        ticket = get_object_or_404(Ticket, pk=pk)
        ticket.assigned_to_id = request.data.get('user_id')
        ticket.save()
        return Response({'assigned': True})
