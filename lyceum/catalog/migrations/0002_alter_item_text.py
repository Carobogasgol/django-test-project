# Generated by Django 4.2.5 on 2023-11-15 19:20

import catalog.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(
                help_text='Описание должно содержать слова "превосходно" или "роскошно"',
                validators=[
                    catalog.validators.WordsValidator(
                        'превосходно', 'роскошно'
                    )
                ],
                verbose_name='описание',
            ),
        ),
    ]