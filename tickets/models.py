from django.db import models
from users.models import User

class Ticket(models.Model):
    STATUS_OPEN = 'OPEN'
    STATUS_IN_PROGRESS = 'IN_PROGRESS'
    STATUS_CLOSED = 'CLOSED'

    STATUS_CHOICES = [
        (STATUS_OPEN, 'Abierto'),
        (STATUS_IN_PROGRESS, 'En progreso'),
        (STATUS_CLOSED, 'Cerrado'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_OPEN
    )

    created_at = models.DateTimeField(auto_now_add=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    assigned_to = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assigned_tickets'
    )

    def __str__(self):
        return f"{self.title} ({self.status})"
