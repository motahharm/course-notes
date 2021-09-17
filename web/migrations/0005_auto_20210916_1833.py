# Generated by Django 3.2.7 on 2021-09-16 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_rename_course_key_model_lesson_model'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson_model',
            old_name='description',
            new_name='key',
        ),
        migrations.RemoveField(
            model_name='lesson_model',
            name='title',
        ),
        migrations.AddField(
            model_name='lesson_model',
            name='value',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]