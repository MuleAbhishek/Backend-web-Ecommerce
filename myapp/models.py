from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name
    # class Meta:
    #     verbose_name_plural = "Contact Table"
