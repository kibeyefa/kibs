# Generated by Django 3.2.12 on 2022-03-22 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0006_pollingunit_polling_unit_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollingunit',
            name='date_entered',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
