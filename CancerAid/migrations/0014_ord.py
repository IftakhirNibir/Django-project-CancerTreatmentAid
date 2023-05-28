# Generated by Django 3.2.6 on 2022-01-01 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CancerAid', '0013_remove_ambudetails_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.TextField()),
                ('reply', models.TextField(null=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CancerAid.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CancerAid.patient')),
            ],
        ),
    ]