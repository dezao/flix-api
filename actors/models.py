from django.db import models

NATIONALITY_CHOICES = (
    ('USA', 'Estados Unidos'),
    ('BRAZIL', 'Brasil'),
    ('CANADA', 'Canadá')
)


class Actor(models.Model):
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=False, blank=True)
    nationality = models.CharField(max_length=100, blank=True, null=True, choices=NATIONALITY_CHOICES)

    def __str__(self):
        return self.name
