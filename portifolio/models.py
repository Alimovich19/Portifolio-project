from django.db import models

class Logo(models.Model):
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return f"Logo - {self.image.url if self.image else 'No Image'}"

class Skills(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='skills/')
    percent = models.IntegerField()

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    link = models.URLField()

    def __str__(self):
        return self.name

class Experience(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company_logo = models.ImageField(upload_to='experience/')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def start_date_display(self):
        return self.start_date.strftime("%b %Y") if self.start_date else "Unknown"

    def end_date_display(self):
        return self.end_date.strftime('%b %Y') if self.end_date else "Present"

    def __str__(self):
        return self.title

class Contact(models.Model):
    description = models.TextField()
    telegram_account = models.URLField()
    instagram_account = models.URLField()
    github_account = models.URLField()
    gmail_account = models.URLField()

    def __str__(self):
        return self.description
