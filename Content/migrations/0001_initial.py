# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('licence', models.TextField()),
                ('tel', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EduContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('summary', models.TextField()),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FileContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_field', models.FileField(upload_to=b'static')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Grad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('country_rank', models.IntegerField(null=True, blank=True)),
                ('state_rank', models.IntegerField(null=True, blank=True)),
                ('major', models.CharField(max_length=100, null=True, blank=True)),
                ('acc_major', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('results', models.ImageField(null=True, upload_to=b'static/images', blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('school', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'static/images')),
                ('caption', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('image', models.ImageField(upload_to=b'static/images')),
                ('date', models.DateTimeField()),
                ('interviewer', models.CharField(max_length=100, null=True, blank=True)),
                ('header', models.TextField(null=True, blank=True)),
                ('footer', models.TextField(null=True, blank=True)),
                ('grad', models.ForeignKey(to='Content.Grad')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('title_image', models.ImageField(upload_to=b'static/images')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('summary', models.TextField()),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('images', models.ManyToManyField(to='Content.ImageContent', null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('available_times', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PsyContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('summary', models.TextField()),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('image', models.ForeignKey(to='Content.ImageContent')),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('title_image', models.ImageField(upload_to=b'static/images')),
                ('summary', models.TextField()),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('audience', models.TextField(null=True, blank=True)),
                ('audio', models.FileField(null=True, upload_to=b'static', blank=True)),
                ('video', models.FileField(null=True, upload_to=b'static', blank=True)),
                ('where', models.TextField()),
                ('when', models.DateTimeField()),
                ('images', models.ManyToManyField(to='Content.ImageContent', null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='grad',
            name='image',
            field=models.ForeignKey(to='Content.ImageContent'),
        ),
        migrations.AddField(
            model_name='educontent',
            name='files',
            field=models.ManyToManyField(to='Content.FileContent', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='educontent',
            name='image',
            field=models.ForeignKey(blank=True, to='Content.ImageContent', null=True),
        ),
        migrations.AddField(
            model_name='advisor',
            name='image',
            field=models.ForeignKey(to='Content.ImageContent'),
        ),
    ]
