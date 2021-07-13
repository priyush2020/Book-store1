# Generated by Django 3.1.4 on 2021-07-08 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('idno', models.AutoField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
            ],
        ),
    ]
