# Generated by Django 3.1.5 on 2021-12-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_application', '0006_selfhelparticle_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selfhelparticle',
            name='article_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
