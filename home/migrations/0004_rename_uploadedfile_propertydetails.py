# Generated by Django 4.2.9 on 2024-03-04 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_uploadedfile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UploadedFile',
            new_name='PropertyDetails',
        ),
    ]
