import uuid

from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
<<<<<<< HEAD
                          primary_key=True, editable=False)
=======
                    primary_key=True, editable=False)
>>>>>>> 1e45d0d7f257b304fda1eea76fef1544c53a4d41

    def __str__(self):
        return self.title
