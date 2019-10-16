# Generated by Django 2.2.6 on 2019-10-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('momo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='momorequest',
            name='financialTransactionId',
            field=models.CharField(default='', help_text='Financial Transaction ID from MTN', max_length=200),
        ),
        migrations.AlterField(
            model_name='momorequest',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='momorequest',
            name='currency',
            field=models.CharField(default='', help_text='Insert Customer Mobile (256********', max_length=3),
        ),
        migrations.AlterField(
            model_name='momorequest',
            name='reqtyp',
            field=models.CharField(default='Collection', help_text='Insert Request Type', max_length=200),
        ),
        migrations.AlterField(
            model_name='momorequest',
            name='status',
            field=models.CharField(default='Pending', help_text='Insert status', max_length=200),
        ),
    ]
