# Generated by Django 3.0.8 on 2020-07-27 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='note',
            field=models.TextField(null=True),
        ),
    ]
