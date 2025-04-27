from django.test import TestCase
from django.utils import timezone
from .models import Category, Article

class CategoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Category.objects.create(category='Innovations', slug='innovations')

    def test_category_str(self):
        category = Category.objects.get(id=1)
        self.assertEqual(str(category), 'Innovations')

    def test_category_get_absolute_url(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.get_absolute_url(), '/articles/category/innovations')


class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(category='Tech', slug='tech')
        cls.article = Article.objects.create(
            title='My Article',
            description='Test content',
            pub_date=timezone.now(),
            category=cls.category,
            main_page=True
        )

    def test_article_str(self):
        self.assertEqual(str(self.article), 'My Article')

    def test_article_slug_auto_generated(self):
        self.assertEqual(self.article.slug, 'my-article')

    def test_article_get_absolute_url(self):
        url = self.article.get_absolute_url()
        self.assertIn('/articles/', url)
        self.assertIn(self.article.slug, url)
