from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    clan = models.CharField(max_length=50, blank=True)
    allegiance = models.CharField(max_length=50, blank=True)
    rank = models.CharField(max_length=50, blank=True)
    occupation = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=50, blank=True)   # add this
    age = models.IntegerField(blank=True, null=True)           # add this
    color = models.CharField(max_length=20, blank=True)        # add this

    def __str__(self):
        return self.name

class Post(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)
    content = models.TextField()
    color = models.CharField(max_length=20, default="blue")
    image = models.CharField(max_length=100, default="images/default.jpg")  # ✅ Add this

    def __str__(self):
        return f"{self.profile.name} - {self.content[:20]}"
