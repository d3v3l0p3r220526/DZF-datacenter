# Generated by Django 4.2.7 on 2024-02-25 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_datecompleted_alter_task_documentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='documentId',
            field=models.IntegerField(),
        ),
    ]
