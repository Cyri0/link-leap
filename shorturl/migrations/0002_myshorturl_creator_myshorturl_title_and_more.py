# Generated by Django 4.2.6 on 2023-10-19 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shorturl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myshorturl',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='myshorturl',
            name='title',
            field=models.CharField(default='old', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myshorturl',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
