# Generated by Django 3.1 on 2020-09-12 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0002_auto_20200829_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='envoy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cases', to=settings.AUTH_USER_MODEL, verbose_name='Case Envoy'),
        ),
    ]
