# Generated by Django 5.0 on 2023-12-28 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_alter_member_country_alter_member_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]
