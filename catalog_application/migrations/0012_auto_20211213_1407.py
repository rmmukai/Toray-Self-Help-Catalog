# Generated by Django 3.1.5 on 2021-12-13 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_application', '0011_auto_20211208_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selfhelparticle',
            name='article_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
