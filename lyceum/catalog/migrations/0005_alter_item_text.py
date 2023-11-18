# Generated by Django 4.2.5 on 2023-11-15 21:17

import catalog.validators
import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('catalog', '0004_alter_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=ckeditor.fields.RichTextField(
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
