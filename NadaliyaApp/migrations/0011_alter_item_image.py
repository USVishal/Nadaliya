# Generated by Django 4.2.3 on 2023-07-26 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NadaliyaApp', '0010_item_user_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(default='static/images/default.png', upload_to='images/items'),
        ),
    ]
