from django.contrib import admin
from .models import News
from .models import Category
from .models import *


admin.site.register(News)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Comment)





# Register your models here.
