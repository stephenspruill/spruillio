# Generated by Django 3.2.7 on 2021-09-16 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spruillio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='preview_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
