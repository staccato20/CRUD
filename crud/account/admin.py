from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserCreationForm
    model = CustomUserCreationForm

    fieldsets = (
        (None, {'fields' : ('username', 'password')}),
        ('Personal info', {'fields' : ('first_name', 'email', 'age', 'address')}),
        ('Permissions', {
            'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields' : ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('username', 'email', 'age', 'address', 'password1', 'password2'),
        }),
    )

    list_display = ('username', 'email', 'age', 'address', 'first_name', 'last_name', 'is_staff')

admin.site.register(CustomUser, CustomUserCreationForm)

