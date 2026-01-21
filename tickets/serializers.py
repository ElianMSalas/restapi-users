from rest_framework import serializers
from .models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.email')
    assigned_to = serializers.ReadOnlyField(source='assigned_to.email')

    class Meta:
        model = Ticket
        fields = (
            'id',
            'title',
            'description',
            'status',
            'created_at',
            'created_by',
            'assigned_to',
        )
