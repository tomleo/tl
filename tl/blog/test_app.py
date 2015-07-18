from django.test import TestCase

from . import views
from .factories import PostFactory

class TestPostDetailView(TestCase):

    def test_invalid_post(self):
        post = PostFactory.create()
        response = client.get(reverse('post-detail', kwargs={ 'pk': post.id+1 }))
        self.assertEqual(response.status_code, 404)

    def test_valid_post(self):
        response = client.get(reverse('post-detail', kwargs={ 'pk': post.id }))
        self.assertEqual(response.status_code, 200)


