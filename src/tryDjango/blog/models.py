from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title       =       models.CharField(max_length=120)
    description =       models.TextField(blank=True)
    featured    =       models.BooleanField()

    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"pk": self.pk})
    

