# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 03:22
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import user_related.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(error_messages={'unique': '该邮箱已注册！'}, max_length=50, unique=True, validators=[django.core.validators.RegexValidator('\\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z0-9.-]+')], verbose_name='电子邮件地址')),
                ('name', models.CharField(error_messages={'required': '您的大名是必须要填的～'}, max_length=10, validators=[django.core.validators.RegexValidator('[\\u4e00-\\u9fa5]{2,4}')], verbose_name='姓名')),
                ('phone', models.CharField(error_messages={'required': '您的手机号是必须填的~', 'unique': '您输入的手机号已存在～'}, max_length=11, unique=True, validators=[django.core.validators.RegexValidator('1\\d{10}', '请输入正常的手机号～～')], verbose_name='手机号')),
                ('nick_name', models.CharField(blank=True, max_length=30, verbose_name='昵称')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='注册日期')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'ordering': ('name',),
                'verbose_name_plural': '用户',
                'abstract': False,
            },
            managers=[
                ('objects', user_related.models.UserManager()),
            ],
        ),
    ]