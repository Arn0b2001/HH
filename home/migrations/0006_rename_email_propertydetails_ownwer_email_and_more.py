# Generated by Django 4.2.9 on 2024-03-04 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_propertydetails_email_alter_signup_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertydetails',
            old_name='email',
            new_name='ownwer_email',
        ),
        migrations.RenameField(
            model_name='propertydetails',
            old_name='image',
            new_name='p_image',
        ),
    ]
