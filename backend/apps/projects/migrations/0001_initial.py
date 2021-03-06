# Generated by Django 3.1 on 2020-08-22 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('meta', '0002_auto_20200822_1204'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=128, verbose_name='Project title')),
                ('start_date', models.DateField(null=True, verbose_name='Start Date')),
                ('end_date', models.DateField(null=True, verbose_name='End Date')),
                ('description', models.TextField(blank=True, help_text='Long description for the Project', verbose_name='Project description')),
                ('case_types', models.ManyToManyField(related_name='project_case_types', to='meta.CaseType')),
                ('envoys', models.ManyToManyField(related_name='project_envoys', to=settings.AUTH_USER_MODEL)),
                ('project_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meta.projectclass', verbose_name='Project Class')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', model_utils.fields.AutoCreatedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(db_index=True, default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('code', models.SlugField(max_length=128, unique=True, verbose_name='Code')),
                ('famous_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Name')),
                ('mobile', models.CharField(blank=True, max_length=32, null=True, verbose_name='Mobile')),
                ('address', models.CharField(blank=True, max_length=150, null=True, verbose_name='Address')),
                ('national_id', models.CharField(blank=True, max_length=32, null=True, verbose_name='National ID')),
                ('description', models.TextField(blank=True, help_text='Long description for the Case', verbose_name='Description')),
                ('envoy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Case Envoy')),
                ('problems', models.ManyToManyField(related_name='case_problems', to='meta.Problem')),
                ('types', models.ManyToManyField(related_name='case_types', to='meta.CaseType')),
            ],
            options={
                'verbose_name': 'Case',
                'verbose_name_plural': 'Cases',
            },
        ),
    ]
