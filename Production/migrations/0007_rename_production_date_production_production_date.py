# Generated by Django 4.2.3 on 2023-07-19 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Production', '0006_alter_production_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='production',
            old_name='production_Date',
            new_name='production_date',
        ),
    ]