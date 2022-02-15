# Generated by Django 4.0.2 on 2022-02-15 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MakeMyDegree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MakeMyDegree.course')),
                ('tag_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MakeMyDegree.tag')),
            ],
        ),
    ]
