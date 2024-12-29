from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Blog,
		Portfolio,
		Testimonials,
		Certificate, 
		WorkExperience, 
		Skill,
	)

from django.views import generic


from . forms import ContactForm

from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonials,
    Certificate,
    WorkExperience,
    Skill,  # Add Skill model here
)

class Home(generic.TemplateView):
	template_name = "portfolio/index.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

        # Add Skill objects to the context
		user_profile = UserProfile.objects.first()

		context["me"] = user_profile.user

		context["skills"] = Skill.objects.filter(userprofile=user_profile)
        
        # Debug print to check what skills are being passed
		print("Skills being passed to template:", list(context["skills"].values_list('name', 'is_key_skill')))
        
		#skills = Skill.objects.all()  # Query all Skill objects

		testimonials = Testimonials.objects.filter(is_active=True)
		certificates = Certificate.objects.filter(is_active=True)
		blogs = Blog.objects.filter(is_active=True)
		portfolio = Portfolio.objects.filter(is_active=True)
		work_experiences = WorkExperience.objects.all()

		#context["skills"] = skills  # Add skills to context
		context["testimonials"] = testimonials
		context["certificates"] = certificates
		context["blogs"] = blogs
		context["portfolio"] = portfolio
		context["work_experiences"] = work_experiences

		return context


class ContactView(generic.FormView):
	template_name = "portfolio/contact.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)


class PortfolioView(generic.ListView):
	model = Portfolio
	template_name = "portfolio/portfolio.html"
	paginate_by = 10

	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class PortfolioDetailView(generic.DetailView):
	model = Portfolio
	template_name = "portfolio/portfolio-detail.html"

class BlogView(generic.ListView):
	model = Blog
	template_name = "portfolio/blog.html"
	paginate_by = 10
	
	def get_queryset(self):
		return super().get_queryset().filter(is_active=True)


class BlogDetailView(generic.DetailView):
	model = Blog
	template_name = "portfolio/blog-detail.html"