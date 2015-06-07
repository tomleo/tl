from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.urlresolvers import reverse


class Technology(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    about = models.TextField()

    class Meta:
        abstract = True
        ordering = ['name']


class Category(Technology):
    pass


class Framework(Technology):
    pass


class Lanuage(Technology):
    pass


class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    languages = models.ManyToManyField(Lanuage, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    framework = models.ManyToManyField(Framework, blank=True)

    class Meta:
        ordering = ['start_date', 'name']

    def __str__(self):
        return u'{}'.format(self.slug)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.id, 'slug': self.slug})