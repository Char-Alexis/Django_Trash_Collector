# Generated by Django 3.2.5 on 2021-08-31 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_alter_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='weekly_pickup_day',
            field=models.CharField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday')], default='Monday', max_length=10),
        ),
    ]
