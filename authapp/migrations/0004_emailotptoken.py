# Generated by Django 4.0.1 on 2024-05-23 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_user_is_lecturer'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailOTPToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp_code', models.CharField(max_length=4)),
                ('otp_created_at', models.DateTimeField(auto_now_add=True)),
                ('otp_expires_at', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_otps', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]