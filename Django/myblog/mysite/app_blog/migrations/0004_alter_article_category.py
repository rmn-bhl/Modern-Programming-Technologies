# Generated by Django 5.1.7 on 2025-03-30 21:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_blog", "0003_alter_article_options_alter_article_slug_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="articles",
                to="app_blog.category",
                verbose_name="Категорія",
            ),
            preserve_default=False,
        ),
    ]
