# Generated by Django 4.2.3 on 2023-08-01 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
