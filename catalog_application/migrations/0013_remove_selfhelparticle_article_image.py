# Generated by Django 3.1.5 on 2022-01-25 00:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_application', '0012_auto_20211213_1407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selfhelparticle',
            name='article_image',
        ),
    ]
