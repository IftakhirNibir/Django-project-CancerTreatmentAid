# Generated by Django 3.2.6 on 2022-01-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CancerAid', '0029_auto_20220108_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.CharField(choices=[('You will get 30 percent discount', 'You will get 30 percent discount'), ('You will get 50 percent discount', 'You will get 50 percent discount'), ('You will get 70 percent discount', 'You will get 70 percent discount'), ('Sorry there is no discount for you', 'Sorry there is no discount for you')], max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Discount',
        ),
    ]
