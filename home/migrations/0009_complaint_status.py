# Generated by Django 4.2.9 on 2024-04-23 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_booking_complaint_complaint_book_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='status',
            field=models.CharField(default='close', max_length=50),
        ),
    ]