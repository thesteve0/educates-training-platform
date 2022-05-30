# Generated by Django 3.2.13 on 2022-05-29 23:41

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import project.apps.workshops.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        migrations.swappable_dependency(settings.OAUTH2_PROVIDER_APPLICATION_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Environment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop_name', models.CharField(max_length=256, verbose_name='workshop name')),
                ('name', models.CharField(default='', max_length=255, verbose_name='environment name')),
                ('uid', models.CharField(default='', max_length=255, verbose_name='resource uid')),
                ('state', models.IntegerField(choices=[(1, 'STARTING'), (2, 'RUNNING'), (3, 'STOPPING'), (4, 'STOPPED')], default=project.apps.workshops.models.EnvironmentState['STARTING'])),
                ('position', models.IntegerField(default=0, verbose_name='index position')),
                ('capacity', models.IntegerField(default=0, verbose_name='maximum capacity')),
                ('initial', models.IntegerField(default=0, verbose_name='initial instances')),
                ('reserved', models.IntegerField(default=0, verbose_name='reserved instances')),
                ('expires', models.DurationField(default=datetime.timedelta(0), verbose_name='workshop duration')),
                ('overtime', models.DurationField(default=datetime.timedelta(0), verbose_name='overtime period')),
                ('deadline', models.DurationField(default=datetime.timedelta(0), verbose_name='maximum deadline')),
                ('orphaned', models.DurationField(default=datetime.timedelta(0), verbose_name='inactivity timeout')),
                ('tally', models.IntegerField(default=0, verbose_name='workshop tally')),
                ('env', project.apps.workshops.models.JSONField(default=[], verbose_name='environment overrides')),
            ],
        ),
        migrations.CreateModel(
            name='TrainingPortal',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='portal name')),
                ('uid', models.CharField(default='', max_length=255, verbose_name='resource uid')),
                ('generation', models.IntegerField(default=0, verbose_name='generation')),
                ('sessions_maximum', models.IntegerField(default=0, verbose_name='sessions maximum')),
                ('sessions_registered', models.IntegerField(default=0, verbose_name='sessions registered')),
                ('sessions_anonymous', models.IntegerField(default=0, verbose_name='sessions anonymous')),
                ('default_capacity', models.IntegerField(default=0, verbose_name='default capacity')),
                ('default_reserved', models.IntegerField(default=None, null=True, verbose_name='default reserved')),
                ('default_initial', models.IntegerField(default=None, null=True, verbose_name='default initial')),
                ('default_expires', models.CharField(default='', max_length=32, verbose_name='default expires')),
                ('default_overtime', models.CharField(default='', max_length=32, verbose_name='default overtime')),
                ('default_deadline', models.CharField(default='', max_length=32, verbose_name='default deadline')),
                ('default_orphaned', models.CharField(default='', max_length=32, verbose_name='default orphaned')),
                ('update_workshop', models.BooleanField(default=False, verbose_name='workshop updates')),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='workshop name')),
                ('uid', models.CharField(max_length=255, verbose_name='resource uid')),
                ('generation', models.IntegerField(verbose_name='generation')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('vendor', models.CharField(max_length=128)),
                ('authors', project.apps.workshops.models.JSONField(default=[])),
                ('difficulty', models.CharField(max_length=128)),
                ('duration', models.CharField(max_length=128)),
                ('tags', project.apps.workshops.models.JSONField(default=[])),
                ('logo', models.TextField()),
                ('url', models.CharField(max_length=255)),
                ('content', project.apps.workshops.models.JSONField(default={})),
                ('ingresses', project.apps.workshops.models.JSONField(default=[], verbose_name='session ingresses')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('name', models.CharField(max_length=256, primary_key=True, serialize=False, verbose_name='session name')),
                ('id', models.CharField(max_length=64)),
                ('state', models.IntegerField(choices=[(1, 'STARTING'), (2, 'WAITING'), (3, 'RUNNING'), (4, 'STOPPING'), (5, 'STOPPED')], default=project.apps.workshops.models.SessionState['STARTING'])),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('started', models.DateTimeField(blank=True, null=True)),
                ('expires', models.DateTimeField(blank=True, null=True)),
                ('token', models.CharField(blank=True, max_length=256, null=True)),
                ('url', models.URLField(null=True, verbose_name='session url')),
                ('application', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.OAUTH2_PROVIDER_APPLICATION_MODEL)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workshops.environment')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='environment',
            name='portal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='workshops.trainingportal'),
        ),
        migrations.AddField(
            model_name='environment',
            name='workshop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='workshops.workshop'),
        ),
    ]
