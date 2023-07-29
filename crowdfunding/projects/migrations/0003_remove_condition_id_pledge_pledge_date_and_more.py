# Generated by Django 4.2.3 on 2023-07-29 11:00

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_pledge_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condition',
            name='id',
        ),
        migrations.AddField(
            model_name='pledge',
            name='pledge_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 29, 11, 0, 46, 123113, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='condition',
            name='pledge',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='projects.pledge'),
        ),
    ]
