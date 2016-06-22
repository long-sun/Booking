# coding = utf8
from django import forms
from user_related.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset
from crispy_forms.bootstrap import StrictButton, PrependedText


class UserForm(forms.ModelForm):
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(),
        max_length=16,
        required=True,
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'phone')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Fieldset(
                "请输入您的注册信息",
                PrependedText('email', '@', placeholder="请输入您的邮箱地址"),
                Field('password', placeholder="请输入您的密码"),
                Field('phone', placeholder="请输入您的手机号"),
                Field('name', placeholder="请输入您的姓名"),
            )
        )








