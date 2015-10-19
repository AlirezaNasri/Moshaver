# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('email', models.EmailField(max_length=75)),
                ('position', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
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
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FileContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_field', models.FileField(upload_to=b'')),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('country_rank', models.IntegerField()),
                ('state_rank', models.IntegerField()),
                ('major', models.CharField(max_length=100)),
                ('acc_major', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('results', models.ImageField(upload_to=b'')),
                ('city', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageContent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'')),
                ('caption', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('image', models.ImageField(upload_to=b'')),
                ('date', models.DateTimeField()),
                ('interviewer', models.CharField(max_length=100)),
                ('header', models.TextField()),
                ('footer', models.TextField()),
                ('grad', models.ForeignKey(to='Content.Grad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('title_image', models.ImageField(upload_to=b'')),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('summary', models.TextField()),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('images', models.ManyToManyField(to='Content.ImageContent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tel', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('available_times', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
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
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('title_image', models.ImageField(upload_to=b'')),
                ('summary', models.TextField()),
                ('body', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('audience', models.TextField()),
                ('audio', models.FileField(upload_to=b'')),
                ('video', models.FileField(upload_to=b'')),
                ('where', models.TextField()),
                ('when', models.DateTimeField()),
                ('images', models.ManyToManyField(to='Content.ImageContent')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='grad',
            name='image',
            field=models.ForeignKey(to='Content.ImageContent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='educontent',
            name='files',
            field=models.ManyToManyField(to='Content.FileContent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='educontent',
            name='image',
            field=models.ForeignKey(to='Content.ImageContent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advisor',
            name='image',
            field=models.ForeignKey(to='Content.ImageContent'),
            preserve_default=True,
        ),
    ]
