# Generated by Django 4.0.2 on 2022-04-20 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MakeMyDegree', '0002_alter_course_terms'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]