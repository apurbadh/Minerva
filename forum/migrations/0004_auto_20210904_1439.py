# Generated by Django 3.2.7 on 2021-09-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20210903_1959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.ManyToManyField(to='forum.Answer'),
        ),
    ]
