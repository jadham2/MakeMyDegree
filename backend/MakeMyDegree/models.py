from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    degree = models.ForeignKey(
        'Degree',
        on_delete=models.CASCADE,
    )
    curr_plan = models.JSONField()


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    course_tag = models.CharField(max_length=15)
    course_credits = models.IntegerField()
    description = models.TextField()
    terms = ArrayField(
        base_field=models.CharField(max_length=6),
        default=list,
        blank=True
    )


class Requisite(models.Model):
    requisite_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name="courses"
    )
    course_requisite = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
        related_name="requisites"
    )
    requisite_type = models.CharField(max_length=3)


class Degree(models.Model):
    degree_id = models.AutoField(primary_key=True)
    degree_type = models.CharField(max_length=50)
    degree_name = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    term = models.CharField(max_length=50)


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    degree = models.ForeignKey(
        'Degree',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    rule = models.CharField(max_length=50)


class CourseTag(models.Model):
    course_tag_id = models.AutoField(primary_key=True)
    tag_id = models.ForeignKey(
        'Tag',
        on_delete=models.CASCADE,
    )
    course_id = models.ForeignKey(
        'Course',
        on_delete=models.CASCADE,
    )
