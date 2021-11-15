from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
import re


class StudentManager(BaseUserManager):
    use_in_migrations = True

    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        isValidEmailReg = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
        if not email:
            raise ValueError(_('The Email must be set'))
        if not re.match(isValidEmailReg, email):
            raise ValueError(_('Incorrect Email'))
        # if not surname:
        #     raise ValueError(_('The Surname must be set'))
        # if not name:
        #     raise ValueError(_('The Name must be set'))
        # # if not lastname:
        # #     raise ValueError(_('The Lastname must be set'))
        # if not password:
        #     raise ValueError(_('The Password must be set'))
        
        # user = self.model(
        #     email = self.normalize_email(email),
        #     surname = surname,
        #     name = name,
        #     lastname = lastname,
        # )
        # user.set_password(password)

        # extra_fields.setdefault('is_staff', False)
        # extra_fields.setdefault('is_superuser', False)
        # extra_fields.setdefault('is_active', False)

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)