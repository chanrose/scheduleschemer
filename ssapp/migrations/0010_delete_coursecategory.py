# Generated by Django 3.2 on 2021-05-16 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssapp', '0009_remove_faculty_short_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CourseCategory',
        ),
    ]