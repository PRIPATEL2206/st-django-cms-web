# Generated by Django 4.2.3 on 2023-12-21 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsuser',
            name='email',
            field=models.EmailField(default='xyz@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
