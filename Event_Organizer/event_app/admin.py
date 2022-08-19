from django.contrib import admin

from event_app.models import BookEvent, Business, Charity, ContactUs, Culture, Family

# Register your models here.
admin.site.register(Family)
admin.site.register(Culture)
admin.site.register(Charity)
admin.site.register(Business)
admin.site.register(BookEvent)
admin.site.register(ContactUs)