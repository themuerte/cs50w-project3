# Generated by Django 3.2.9 on 2021-12-21 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20211221_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=20),
            preserve_default=False,
        ),
    ]
