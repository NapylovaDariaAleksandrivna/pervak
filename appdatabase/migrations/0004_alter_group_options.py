# Generated by Django 4.2 on 2023-07-11 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appdatabase', '0003_remove_group_course_group_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
    ]