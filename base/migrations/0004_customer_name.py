# Generated by Django 4.0.2 on 2022-04-04 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
