# Generated by Django 5.1.2 on 2024-11-07 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='alert_status',
            field=models.CharField(choices=[('ongoing', 'Ongoing'), ('dismissed', 'Dismissed'), ('pending', 'Pending'), ('done', 'Done')], default='pending', max_length=100, null=True),
        ),
    ]
