# Generated by Django 4.0.4 on 2022-05-02 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0002_alter_offer_bank_delete_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='payment',
            field=models.FloatField(default=0, verbose_name='Ежемесячный платёж'),
        ),
    ]