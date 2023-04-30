# Generated by Django 3.2 on 2023-04-27 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_location_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='url',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
