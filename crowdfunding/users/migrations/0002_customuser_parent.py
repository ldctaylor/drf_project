# Generated by Django 4.2.3 on 2023-08-01 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='parent',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]