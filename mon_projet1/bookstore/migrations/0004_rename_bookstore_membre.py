# Generated by Django 5.1.7 on 2025-03-15 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_rename_membres_bookstore'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bookstore',
            new_name='membre',
        ),
    ]
