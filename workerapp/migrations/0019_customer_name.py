# Generated by Django 5.0 on 2024-08-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workerapp', '0018_alter_worker_is_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
