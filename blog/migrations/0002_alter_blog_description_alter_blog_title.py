# Generated by Django 4.1 on 2022-09-30 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(default='I am Fanilo, a developer from Onja Madagascar', max_length=500),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='About me', max_length=200),
        ),
    ]