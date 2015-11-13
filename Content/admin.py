from django.contrib import admin
from Content.models import News, ImageContent, Workshop, PsyContent, Interview, EduContent, FAQ

admin.site.register(News)
admin.site.register(Workshop)
admin.site.register(PsyContent)
admin.site.register(Interview)
admin.site.register(EduContent)
admin.site.register(FAQ)
admin.site.register(ImageContent)
