# Generated by Django 4.2.7 on 2024-03-04 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_documentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='documentId',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
