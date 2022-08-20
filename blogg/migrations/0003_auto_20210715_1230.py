# Generated by Django 2.2.14 on 2021-07-15 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0002_auto_20210715_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_comment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blogg.post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]