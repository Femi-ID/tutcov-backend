# Generated by Django 4.2.5 on 2023-09-25 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutdb', '0003_alter_user_managers_token_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
