# Generated by Django 4.2 on 2023-07-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdatabase', '0011_feedback_lesson_alter_feedback_name_group_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='lesson',
            field=models.CharField(max_length=40),
        ),
    ]
