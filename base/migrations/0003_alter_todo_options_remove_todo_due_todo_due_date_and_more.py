# Generated by Django 5.0.3 on 2024-04-03 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_todo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-done', '-due_date', '-due_time', '-updated', '-created']},
        ),
        migrations.RemoveField(
            model_name='todo',
            name='due',
        ),
        migrations.AddField(
            model_name='todo',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='due_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]