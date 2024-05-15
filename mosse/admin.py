from django.contrib import admin
from .models import Blog, About, Contact, Subscription, Tag, Comments
# Register your models here.

admin.site.register(Blog)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Subscription)
admin.site.register(Tag)
admin.site.register(Comments)