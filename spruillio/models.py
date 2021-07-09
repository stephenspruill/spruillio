from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    preview_image = models.ImageField(blank=True, null=True)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=200, null=True)

    class Meta:
        db_table = "projects"

    def __str__(self):
        return self.title