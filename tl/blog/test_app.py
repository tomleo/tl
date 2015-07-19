from django.test import TestCase
from django.core.urlresolvers import reverse

from . import views
from .factories import PostFactory

class TestPostDetailView(TestCase):

    def setUp(self):
        self.post = PostFactory.create()

    def test_invalid_post(self):
        response = self.client.get(reverse('post-detail', kwargs={ 'pk': self.post.id+1 }))
        self.assertEqual(response.status_code, 404)

    def test_valid_post(self):
        response = self.client.get(reverse('post-detail', kwargs={ 'pk': self.post.id }))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_create(self):
        response = self.client.post(reverse('post-detail'))

    def test_post_detail_delete(self):
        pass
