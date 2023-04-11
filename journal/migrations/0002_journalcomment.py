# Generated by Django 3.2.16 on 2023-04-01 20:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='NAME')),
                ('comment', models.TextField(verbose_name='COMMENT')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='CREATED DATE')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='journal.journalpost', verbose_name='ARTICLE')),
            ],
        ),
    ]