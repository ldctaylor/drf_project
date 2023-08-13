# Generated by Django 4.2.3 on 2023-08-13 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_condition_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condition',
            name='pledge',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='condition', to='projects.pledge'),
        ),
    ]