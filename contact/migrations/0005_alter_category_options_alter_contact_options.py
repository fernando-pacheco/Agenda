# Generated by Django 4.2.2 on 2023-06-20 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_category_contact_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contato', 'verbose_name_plural': 'Contatos'},
        ),
    ]
