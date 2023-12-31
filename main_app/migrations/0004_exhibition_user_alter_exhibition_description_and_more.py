# Generated by Django 4.2.3 on 2023-09-20 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0003_exhibition'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='description',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='exhibition',
            name='feedback',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='description',
            field=models.TextField(max_length=800),
        ),
    ]
