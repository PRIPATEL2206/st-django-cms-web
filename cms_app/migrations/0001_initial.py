# Generated by Django 4.2.3 on 2023-12-20 05:47

import cms_app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_buyed', models.BooleanField(default=False)),
                ('cart_making_date', models.DateTimeField(auto_now_add=True)),
                ('buying_date', models.DateTimeField(null=True)),
                ('total_prize', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CMSUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default='')),
                ('role', models.CharField(default='Customer', max_length=30)),
                ('role_ID', models.PositiveSmallIntegerField(default=1)),
                ('contect_number', models.CharField(max_length=20)),
                ('balance', models.BigIntegerField(default=10000)),
                ('profile_img', models.ImageField(null=True, upload_to=cms_app.models.upload_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(null=True, upload_to=cms_app.models.upload_path)),
                ('prize', models.PositiveIntegerField(default=0)),
                ('discription', models.TextField(default='')),
                ('quntity', models.PositiveSmallIntegerField(default=0)),
                ('added_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_prize', models.PositiveIntegerField(default=0)),
                ('address', models.TextField(default='')),
                ('status', models.CharField(max_length=100)),
                ('status_code', models.PositiveSmallIntegerField(default=0)),
                ('discription', models.TextField(default='')),
                ('remark', models.TextField(default='')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Customer', to='cms_app.cmsuser')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms_app.cart')),
                ('validator_employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='validatore', to='cms_app.cmsuser')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cms_app.cmsuser'),
        ),
    ]
