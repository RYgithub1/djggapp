# Generated by Django 3.2.16 on 2023-03-19 21:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JournalCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='CATEGORY NAME')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='CREATED DATE')),
            ],
        ),
        migrations.CreateModel(
            name='JournalPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='TITLE')),
                ('text', models.TextField(verbose_name='TEXT')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='CREATED DATE')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='journal.journalcategory', verbose_name='CATEGORY')),
            ],
        ),
    ]