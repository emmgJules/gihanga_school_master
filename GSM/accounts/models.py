from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    MASTER = 1
    DEAN_OF_STUDY = 2
    ACCOUNTANT = 3
    LIBRARIAN = 4
    HARDWARE_MANAGER = 5
    TEACHER = 6
    STUDENT = 7

    ROLE_CHOICES = [
        (MASTER, 'Master'),
        (DEAN_OF_STUDY, 'Dean of Study'),
        (ACCOUNTANT, 'Accountant'),
        (LIBRARIAN, 'Librarian'),
        (HARDWARE_MANAGER, 'Hardware Manager'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    ]

    role = models.IntegerField(choices=ROLE_CHOICES, default=STUDENT)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name='custom_users'  # Specify custom related_name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_users'  # Specify custom related_name
    )
