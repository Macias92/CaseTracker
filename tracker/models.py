from django.db import models

# Create your models here.


class Purchaser(models.Model):
    name = models.CharField(max_length=64)


class Referred(models.Model):
    # REFERRERS = (
    #     (0, 'Get Mortgage'),
    #     (1, 'Edinburgh'),
    #     (2, 'Glasgow'),
    #     (3, 'Keller Williams'),
    #     (4, 'Right Advice'),
    #     (5, 'CP'),
    #     (6, 'AP'),
    #
    # )
    # name = models.IntegerField(choices=REFERRERS)
    #
    # def __str__(self):
    #     return self.get_name_display()

    name = models.CharField(max_length=64)


class Case(models.Model):
    address = models.CharField(max_length=256)
    purchaser = models.ForeignKey(Purchaser, on_delete=models.CASCADE)
    offer_accepted = models.DateField()
    concluded = models.DateField()
    date_of_entry = models.DateField()
    title = models.CharField(max_length=32)
    referred = models.ForeignKey(Referred, on_delete=models.CASCADE)

