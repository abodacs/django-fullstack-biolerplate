# Generated by Django 3.1 on 2020-08-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200820_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Envoy',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Mobile'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text=''),
        ),
    ]
