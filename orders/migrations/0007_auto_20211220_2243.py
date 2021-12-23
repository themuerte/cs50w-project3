# Generated by Django 3.2.9 on 2021-12-20 22:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20211220_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(choices=[('RP', 'regular pizza'), ('SP', 'siciliam pizza'), ('To', 'toppings'), ('ToS', 'toppingsSubs'), ('Su', 'subs'), ('Pa', 'pasta'), ('Sa', 'salads'), ('Di', 'dinner platters')], max_length=5),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('AC', 'Active'), ('FI', 'Finished'), ('WA', 'Waiting')], max_length=5),
        ),
    ]
