# Generated by Django 4.2 on 2023-07-12 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdatabase', '0010_alter_user_name_group_alter_user_name_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='lesson',
            field=models.CharField(default='Предмет', max_length=40),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name_group',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='name_proff',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
