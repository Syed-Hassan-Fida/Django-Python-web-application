# Generated by Django 3.1.4 on 2022-05-30 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_contact_us'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact_us',
            options={'verbose_name': 'Complain / Contact info', 'verbose_name_plural': 'Complain / Contact info'},
        ),
    ]