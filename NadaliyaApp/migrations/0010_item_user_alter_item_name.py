# Generated by Django 4.2.3 on 2023-07-24 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NadaliyaApp', '0009_alter_item_offer_alter_item_price_alter_item_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NadaliyaApp.user_registration'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
