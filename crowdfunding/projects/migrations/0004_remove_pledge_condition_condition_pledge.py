# Generated by Django 4.0.7 on 2023-08-05 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_condition_pledge_pledge_condition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pledge',
            name='condition',
        ),
        migrations.AddField(
            model_name='condition',
            name='pledge',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conditionpledges', to='projects.pledge'),
        ),
    ]
