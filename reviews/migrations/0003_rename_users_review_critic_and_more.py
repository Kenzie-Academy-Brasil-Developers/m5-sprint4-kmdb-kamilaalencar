# Generated by Django 4.0.5 on 2022-06-30 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_alter_review_recomendation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='users',
            new_name='critic',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='movies',
            new_name='movie',
        ),
    ]