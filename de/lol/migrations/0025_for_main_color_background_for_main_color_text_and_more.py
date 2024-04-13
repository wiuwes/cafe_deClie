# Generated by Django 4.0.1 on 2022-04-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0024_remove_for_main_color_background_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='for_main',
            name='color_background',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='for_main',
            name='color_text',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='for_main',
            name='heading',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='for_main',
            name='image',
            field=models.ImageField(null=True, upload_to='for_main'),
        ),
        migrations.AddField(
            model_name='for_main',
            name='text',
            field=models.TextField(null=True),
        ),
    ]