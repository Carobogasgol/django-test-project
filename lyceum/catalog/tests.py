import django.test
import parameterized

import catalog.models


__all__ = []


class StaticUrlTests(django.test.TestCase):
    def test_catalog_endpoint(self):
        response = django.test.Client().get('/catalog/')

        self.assertEqual(response.status_code, 200)

    @parameterized.parameterized.expand(
        [
            ('1', 200),
            ('100', 200),
            ('0', 200),
            ('-0', 404),
            ('-0', 404),
            ('-100', 404),
            ('0.5', 404),
            ('abc', 404),
            ('0abc', 404),
            ('abc0', 404),
            ('$%^', 404),
            ('1e5', 404),
        ],
    )
    def test_catalog_item_endpoint(self, url, expected_status):
        response = django.test.Client().get(f'/catalog/{url}/')
        self.assertEqual(response.status_code, expected_status)


class ModelsTests(django.test.TestCase):
    def setUp(self):
        self.category = catalog.models.Category.objects.create(
            name='Test category',
            slug='test-category',
        )
        self.tag = catalog.models.Tag.objects.create(
            name='Test tag',
            slug='test-tag',
        )
        super(ModelsTests, self).setUp()

    def tearDown(self):
        catalog.models.Item.objects.all().delete()
        catalog.models.Tag.objects.all().delete()
        catalog.models.Category.objects.all().delete()

        super(ModelsTests, self).tearDown()

    @parameterized.parameterized.expand(
        [
            ('Превосходно'),
            ('роскошно'),
            ('роскошно!'),
            ('роскошно©'),
            ('!роскошно'),
            ('не роскошно'),
        ],
    )
    def test_item_validator(self, text):
        items_count = catalog.models.Item.objects.count()

        item = catalog.models.Item(
            name='Тестовый товар',
            text=text,
            category=self.category,
        )
        item.full_clean()
        item.save()
        item.tags.add(self.tag)

        self.assertEqual(catalog.models.Item.objects.count(), items_count + 1)

    @parameterized.parameterized.expand(
        [
            ('Прев!осходно'),
            ('роскошный'),
            ('роскошное!'),
            ('оскошно©'),
            ('р оскошно'),
            ('qwertyроскошно'),
        ],
    )
    def test_item_negative_validator(self, text):
        items_count = catalog.models.Item.objects.count()

        with self.assertRaises(django.core.exceptions.ValidationError):
            item = catalog.models.Item(
                name='Тестовый товар',
                text=text,
                category=self.category,
            )
            item.full_clean()
            item.save()
            item.tags.add(self.tag)
        self.assertEqual(catalog.models.Item.objects.count(), items_count)

    @parameterized.parameterized.expand(
        [
            (-100),
            (0),
            (64000),
        ],
    )
    def test_category_negative_validator(self, weight):
        categories_count = catalog.models.Category.objects.count()

        with self.assertRaises(django.core.exceptions.ValidationError):
            test_category = catalog.models.Category(
                name='Тестовая категория',
                weight=weight,
                slug='test-cat',
            )
            test_category.full_clean()
            test_category.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            categories_count,
        )

    @parameterized.parameterized.expand(
        [
            (1),
            (100),
            (32000),
        ],
    )
    def test_category_validator(self, weight):
        categories_count = catalog.models.Category.objects.count()

        test_category = catalog.models.Category(
            name='Тестовая категория',
            weight=weight,
            slug='test-cat',
        )
        test_category.full_clean()
        test_category.save()
        self.assertEqual(
            catalog.models.Category.objects.count(),
            categories_count + 1,
        )
