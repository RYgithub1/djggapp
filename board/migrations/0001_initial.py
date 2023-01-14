# Generated by Django 4.1.5 on 2023-01-11 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snsTitle', models.CharField(max_length=100)),
                ('snsContent', models.TextField()),
                ('snsAuthor', models.CharField(max_length=50)),
                ('snsImage', models.ImageField(upload_to='')),
                ('snsGood', models.ImageField(upload_to='')),
                ('snsRead', models.ImageField(upload_to='')),
                ('personsWhoRead', models.TextField()),
            ],
        ),
    ]