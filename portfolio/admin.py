from django.contrib import admin
from .models import (
    UserProfile,
    ContactProfile,
    Testimonials,
    Media,
    Portfolio,
    Blog,
    Certificate,
    Skill, 
    WorkExperience
)

from django.contrib import admin

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'description', 'link')
    search_fields = ('category', 'title', 'description')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user')

@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ('id','timestamp','name')

@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('id','is_active')

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('date','name', 'is_active')
    readonly_fields = ('slug',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id',)
    readonly_fields = ('slug',)
@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('title','name')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

