# Generated by Django 4.2.3 on 2023-08-12 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='description',
            field=models.TextField(),
        ),
    ]
