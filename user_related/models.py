# coding = utf8

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.contenttypes.models import ContentType
from django.core import validators
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name, password, phone, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('必须提供邮箱地址！')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name=None, password=None, phone=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, name, password, phone, **extra_fields)

    def create_superuser(self, email, name, password, phone, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, name, password, phone, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        _('电子邮件地址'),
        max_length=50,
        unique=True,
        validators=[
            validators.RegexValidator(
                r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+',
            ),
        ],
        error_messages={
            'unique': _("该邮箱已注册！"),
        },
    )
    name = models.CharField(
        _('姓名'),
        max_length=10,
        validators=[
            validators.RegexValidator(
                r'[\u4e00-\u9fa5]{2,4}',
                _('您的姓名必须为汉字')
            ),
        ],
        error_messages={
            'required': _('务必提供您的真实姓名')
        }
    )
    phone = models.CharField(
        _('手机号'),
        max_length=11,
        unique=True,
        validators=[
            validators.RegexValidator(
                r'1\d{10}',
                _('您的手机号必须为11位，且以数字1开头')
            ),
        ],
        error_messages={
            'required': _('务必提供您的手机号'),
            'unique': _('您输入的手机号已存在'),
        }
    )
    nick_name = models.CharField(
        _('昵称'),
        max_length=30,
        blank=True
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('注册日期'), auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phone']

    class Meta:
        abstract = False
        verbose_name = _('用户')
        verbose_name_plural = _('用户')
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.name, self.nick_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)




