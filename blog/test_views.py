from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post

class TestBlogViews(TestCase):
    
    def setUp(self):
        self.user = USer.objects.create_superuser(
            username = 'myUsername',
            password = "myPassword",
            email = "test@test.com"
        )
        self.post = Post(title="Blog Title", author = self.user, slug="blog-title", 
                         excerpt="Blog excerpt", content="Blog Content", status=1)
        self.post.save()

    def rest_render_post_detail_page_with_comment_form(self):
        response = self.client(reverse(
            'post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm
        )