# Generated by Django 5.1 on 2024-09-03 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_rename_genre_book_genres'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['id', 'title', 'author']},
        ),
    ]
