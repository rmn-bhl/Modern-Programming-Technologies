from django.test import TestCase
from django.urls import reverse, resolve
from app_blog.views import HomePageView, ArticleList, ArticleCategoryList, ArticleDetail

class UrlTests(TestCase):
    def test_home_url(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, HomePageView)

    def test_articles_list_url(self):
        url = reverse('articles-list')
        self.assertEqual(resolve(url).func.view_class, ArticleList)

    def test_articles_category_url(self):
        url = reverse('articles-category-list', kwargs={'slug': 'test-slug'})
        self.assertEqual(resolve(url).func.view_class, ArticleCategoryList)

    def test_article_detail_url(self):
        url = reverse('news-detail', kwargs={
            'year': '2024',
            'month': '04',
            'day': '15',
            'slug': 'test-article'
        })
        self.assertEqual(resolve(url).func.view_class, ArticleDetail)