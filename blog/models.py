from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone

# Create your models here.

class Blog(models.Model):

	pass


class Comment(models.Model):

	pass

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def was_published_recently(self):
		# within one day
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	def __str__(self):
		return self.question_text

class Choice(models.Model):
	# one question can map to several choices
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text

class Post(models.Model):
	STATUS_CHOICES = (
		('draft', 'Draft'),
		('published', 'Published'),
	)
	# post title, CharField -> varchar in SQL
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250, unique_for_date='publish')
	# foreignKey -- many to one relationship -- one user can write several posts
	author = models.ForeignKey(User, related_name='blog_posts',on_delete=models.CASCADE)
	# body of the post
	body = models.TextField()
	# publish time of the post
	publish = models.DateTimeField(default=timezone.now)
	# create time of the post, auto_now -> date will be saved automatically
	created = models.DateTimeField(auto_now_add=True)
	# when the last time a post was updated
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

	# sort results by the publish field in descending order by default
	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title