# Generated by Django 2.2.16 on 2020-09-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('published_at', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('product', models.ManyToManyField(related_name='articles', to='products.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Статью',
                'verbose_name_plural': 'Статьи',
                'ordering': ['-published_at'],
            },
        ),
    ]
