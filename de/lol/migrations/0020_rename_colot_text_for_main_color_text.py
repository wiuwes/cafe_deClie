# Generated by Django 4.0.1 on 2022-04-02 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0019_for_main_alter_reservation_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='for_main',
            old_name='colot_text',
            new_name='color_text',
        ),
    ]