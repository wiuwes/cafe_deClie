# Generated by Django 4.0.1 on 2022-04-02 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lol', '0031_alter_store_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galary',
            name='title',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
