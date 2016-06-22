from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from user_related.models import User


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(label='密码', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password', 'name', 'phone')

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit():
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('password',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class MyUserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('email', 'name', 'phone', 'last_login')
    search_fields = ('email', 'name')
    readonly_fields = ('last_login',)
    fieldsets = (
        (None, {'fields': ('last_login', 'is_staff', 'is_active')}),
        ('Personal info', {'fields': ('email', 'name', 'phone')}),
      )
    ordering = ("name",)

admin.site.register(User, MyUserAdmin)