import django.test
import django.urls

__all__ = []


class StaticUrlTests(django.test.TestCase):
    def test_about_endpoint(self):
        response = django.test.Client().get(
            django.urls.reverse('about:about'),
        )

        self.assertEqual(response.status_code, 200)
