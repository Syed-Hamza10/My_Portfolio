from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters  import slugify
from ckeditor.fields import RichTextField

# Create your models here.

##### New Code Below
class WorkExperience(models.Model):
    CATEGORY_CHOICES = [
        ('preply', 'Preply Tutor'),
        ('freelance', 'Freelance Tutor'),
        ('other', 'Other'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    title = models.CharField(max_length=100, blank=True, null=True)  # Optional title
    description = models.TextField(blank=True, null=True)  # Optional description
    details = models.JSONField(blank=True, null=True)  # Optional JSON field for additional details
    link = models.URLField(blank=True, null=True)  # Optional URL field for links like a Preply profile

    def __str__(self):
        return f"{self.category}: {self.title or 'No Title'}"

##### New Code Above


class Skill(models.Model):
    class Meta:
        verbose_name_plural = 'Skills'
        verbose_name = 'Skill'

    name = models.CharField(max_length = 20, blank = True, null = True)
    score = models.IntegerField(default = 80, blank = True, null = True)
    image = models.FileField(blank = True, null = True,upload_to='skills')
    is_key_skill = models.BooleanField(default = False)    
    def __str__(self):
        return self.name
    
class UserProfile(models.Model):

    class Meta:
        verbose_name_plural = 'User Profiles'

    user = models.OneToOneField(User, on_delete = models.CASCADE)
    avatar = models.ImageField(blank = True, null = True, upload_to='avatar')
    title = models.CharField(max_length = 200, blank = True, null = True)
    bio = models.TextField(blank=True, null = True)
    skills = models.ManyToManyField(Skill,blank = True)
    cv = models.FileField(blank = True, upload_to='cv')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
class ContactProfile(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ['timestamp']    
    timestamp = models.TimeField(auto_now_add = True)
    name = models.CharField(verbose_name = "Name", max_length = 100)
    email = models.EmailField(verbose_name = 'Email')
    message = models.TextField(verbose_name = 'Message')

    def __str__(self):
        return f'{self.name}'
    
class Testimonials(models.Model):

    class Meta:
        verbose_name_plural = 'Testimonials'
        verbose_name = 'Testimonial'
        ordering = ['name']

    name = models.CharField(max_length = 100, blank=True, null = True)
    thumbnail = models.ImageField(blank=True, null = True, upload_to='thumbnail')
    role = models.CharField(max_length = 500,blank=True, null = True)
    quote = models.CharField(max_length = 500, blank=True, null = True)
    is_active = models.BooleanField(default = True, blank=True, null = True)

    def __str__(self):
        return f'{self.name}'
    

class Media(models.Model):

    class Meta:
        verbose_name_plural = 'Media Files'
        verbose_name = "Media File"
        ordering = ['name']

    image = models.ImageField(blank=True, null = True, upload_to='media')
    url = models.URLField(blank=True, null = True)
    name = models.CharField(max_length = 200)
    is_image = models.BooleanField(default = False)

    def save(self,*args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Portfolio(models.Model):

    class Meta:
        verbose_name_plural = 'Portfolio Profiles'
        verbose_name = 'Porfolio'
        ordering = ['name']

    date = models.DateField(blank=True, null = True)
    name = models.CharField(max_length = 200,blank=True, null = True)
    description = models.CharField(max_length=500, blank=True, null = True)
    body = RichTextField(blank=True, null = True)
    image = models.ImageField(upload_to='portfolio', blank=True, null = True)
    slug = models.SlugField(blank=True, null = True)
    is_active = models.BooleanField(default = True, blank=True, null = True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Portfolio,self).save(*args, **kwargs)

    def get_abosulute_url(self):
        return f'/portfolio/{self.slug}'
    
class Blog(models.Model):
    
    class Meta:
        verbose_name_plural = 'Blog'
        verbose_name = 'Blog'
        ordering = ['name']

    date = models.DateField(blank=True, null = True)
    name = models.CharField(max_length = 200,blank=True, null = True)
    description = models.CharField(max_length=500, blank=True, null = True)
    body = RichTextField(blank=True, null = True)
    image = models.ImageField(upload_to='blog', blank=True, null = True)
    slug = models.SlugField(blank=True, null = True)
    is_active = models.BooleanField(default = True, blank=True, null = True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Blog,self).save(*args, **kwargs)

    def get_abosulute_url(self):
        return f'/blog/{self.slug}'   

class Certificate(models.Model):

    class Meta:
        verbose_name_plural = 'Ceertificates'
        verbose_name = 'Certificate'

    date = models.DateTimeField(blank = True , null = True)
    name = models.CharField(max_length=50,blank = True , null = True)    
    title = models.CharField( blank = True , null = True,max_length=50)     
    description = models.CharField(max_length = 200, blank = True , null = True)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name
    






