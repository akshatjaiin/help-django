# Generated by Django 4.2.13 on 2024-07-27 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedi', '0002_animal_pet_user_bio_user_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PetImage',
            new_name='PetPost',
        ),
        migrations.RenameField(
            model_name='pet',
            old_name='is_active',
            new_name='adopt',
        ),
        migrations.RemoveField(
            model_name='pet',
            name='watchlist',
        ),
        migrations.AddField(
            model_name='pet',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
