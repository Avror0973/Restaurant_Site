# Generated by Django 4.0.4 on 2022-05-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_project', '0009_alter_reviews_options_menu_is_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_account',
            name='is_email_verified',
            field=models.BooleanField(default=False),
        ),
    ]