# Generated by Django 2.0.3 on 2018-08-02 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_gamepage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='natpage',
            name='user2',
        ),
        migrations.DeleteModel(
            name='NatPage',
        ),
    ]