# Generated by Django 2.2.16 on 2020-09-15 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
