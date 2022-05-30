from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin



class AccountAdmin(UserAdmin):
	list_display = ('email','name','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')
	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Language)
admin.site.register(Borrower)
admin.site.register(Account, AccountAdmin)
