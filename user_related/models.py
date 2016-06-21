# coding=utf8

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    name = models.CharField(
        _('姓名'),
        max_length=10,
        help_text=_('请输入您的真实姓名'),
        error_messages={
            'required': _("请输入您的真实姓名！"),
        }
    )

    phone = models.CharField(
        _('手机号码'),
        unique=True,
        max_length=11)

    STUDENT_TYPES = (
        (0, 'Master'),
        (1, 'Doctor'),
        (None, '如您不选则无法使用预约等功能'),
    )
    student_type = models.IntegerField(choices=STUDENT_TYPES)
    picture = models.ImageField(
        _('头像'),
        upload_to='UserProfile/picture'
    )
    birthday = models.DateField(
        _('生日'),
    )
    year = models.CharField(
        _('入学年份'),
        max_length=4
    )
    introduct = models.TextField(
        _('自我介绍'),
        blank=True
    )

