# Generated by Django 2.2 on 2022-01-23 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='description',
            field=models.TextField(max_length=1024, null=True),
        ),
    ]