# Generated by Django 3.2 on 2021-05-14 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ssapp', '0004_alter_curriculum_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classschedule',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='class_schedule', serialize=False, to='ssapp.course'),
        ),
    ]
