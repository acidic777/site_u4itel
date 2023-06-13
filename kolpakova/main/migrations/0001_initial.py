# Generated by Django 4.2.1 on 2023-05-19 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nagrad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('file', models.FileField(upload_to='static/main/file', verbose_name='Документ')),
            ],
        ),
        migrations.CreateModel(
            name='Practic1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('file', models.FileField(upload_to='static/main/file', verbose_name='Документ')),
            ],
        ),
        migrations.CreateModel(
            name='Practic2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('file', models.FileField(upload_to='static/main/file', verbose_name='Документ')),
            ],
        ),
        migrations.CreateModel(
            name='Teory1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('file', models.FileField(upload_to='static/main/file', verbose_name='Документ')),
            ],
        ),
        migrations.CreateModel(
            name='Teory2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('file', models.FileField(upload_to='static/main/file', verbose_name='Документ')),
            ],
        ),
    ]