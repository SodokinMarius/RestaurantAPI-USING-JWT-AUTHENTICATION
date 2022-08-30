from django.test import TestCase

# Create your tests here.
''' def create_superuser(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("User must have an username")
        if not password:
            raise ValueError("User must have a password")
        if not name:
            raise ValueError("User must have a full name")

        user = self.model(
            username=self.normalize_email(username)
        )
        user.name = extra_fields['name']
        user.set_password(password)
        user.admin = True
        user.staff = True
        user.active = True
        return user'''