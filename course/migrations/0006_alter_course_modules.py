# Generated by Django 3.2.7 on 2021-09-04 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_course_modules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='modules',
            field=models.ManyToManyField(related_name='module', to='course.Module'),
        ),
    ]
