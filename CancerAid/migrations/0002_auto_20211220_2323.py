# Generated by Django 3.2.6 on 2021-12-20 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CancerAid', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='phone',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='patient',
            name='lname',
            field=models.CharField(max_length=200, null=True),
        ),
    ]