from django.contrib.postgres.fields import JSONField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, _, PermissionsMixin
from django.db.models import ForeignKey


class MemberManager(UserManager):
    pass


class Member(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'),
                              unique=True,
                              error_messages={
                                  'unique': _("A user with that email already exists."),
                              })

    # is_staff = models.BooleanField(_('staff status'), default=False,
    #                                help_text=_('Designates whether the user can log into this admin site.'))

    # objects = MemberManager()

    USERNAME_FIELD = 'email'
    objects = MemberManager()

    # REQUIRED_FIELDS = ['username']

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def __str__(self):
        return self.email


class Order(models.Model):
    restaurant = models.CharField(max_length=50)
    user = ForeignKey(Member, null=True, blank=True)
    foods = JSONField('')
    total_price = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    order_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.restaurant
