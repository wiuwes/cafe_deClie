# Generated by Django 4.0.1 on 2022-02-07 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
