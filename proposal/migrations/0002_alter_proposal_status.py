# Generated by Django 4.2.19 on 2025-03-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('under_review', 'Under Review')], default='pending', max_length=20),
        ),
    ]
