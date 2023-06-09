from django.db import models


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors["name"] = "First name should be at least 2 characters"
        if postData['description'] and len(postData['description']) < 15:
            errors["description"] = "Description should be at least 10 characters if it's added"
        return errors


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()


