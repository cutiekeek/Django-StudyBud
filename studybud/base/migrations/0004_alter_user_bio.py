# Generated by Django 4.1.5 on 2023-01-14 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
