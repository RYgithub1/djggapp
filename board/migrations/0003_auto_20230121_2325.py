# Generated by Django 3.2.16 on 2023-01-21 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_board_snsgood_alter_board_snsread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='personsWhoRead',
            field=models.TextField(blank='True', default='dorami', null='True'),
        ),
        migrations.AlterField(
            model_name='board',
            name='snsGood',
            field=models.IntegerField(blank='True', default='1', null='True'),
        ),
        migrations.AlterField(
            model_name='board',
            name='snsRead',
            field=models.IntegerField(blank='True', default='1', null='True'),
        ),
    ]
