from django.db import models

class User(models.Model):
    ROLE_TYPE = [
        (1, 'Cheef'),
        (2, 'Cheef Helper'),
        (3, 'Waiter'),
        (4, 'Manager')
    ]
    STATUS_TYPE = [
        (1, 'Working'),
        (2, 'Lay Off'),
        (3, 'at Vacation'),
        (4, 'on Probation')
    ]
    username = models.CharField(max_length=20, unique=True, null=False, blank=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=128)
    role = models.IntegerField(choices=ROLE_TYPE, null=False, blank=False, default=3)
    status = models.IntegerField(choices=STATUS_TYPE, null=False, blank=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
