# Generated by Django 3.1.5 on 2021-12-09 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_application', '0008_auto_20211208_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selfhelparticle',
            name='article_image',
            field=models.ImageField(default='default', upload_to=''),
            preserve_default=False,
        ),
    ]
