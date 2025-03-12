from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager

# Custom user manager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        if not username:
            raise ValueError("The Username field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, username, password, **extra_fields)

# Custom user model
class CustomUser (AbstractUser ):
    email = models.EmailField(unique=True)  
    username = models.CharField(max_length=150, unique=True)  
    objects = CustomUserManager()

    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = ["username"]  

    librarian = models.BooleanField(default=False)
    member = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email
    
    