from django.db import models


# Create your models here.
class Card(models.Model):

    STATUS_OPTS = [
        ('Active', 'Active'),
        ('Not Active', 'Not Active'),
        ('Expired', 'Expired')
    ]


    series = models.PositiveIntegerField(null=False, blank=False, default=0000, verbose_name="Card Series")
    number = models.PositiveIntegerField(null=False, blank=False, default=8888, verbose_name="Card Number")
    
    date_created = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField(null=True)
    last_used = models.DateTimeField(auto_now=True)

    balance = models.FloatField(null=False, default=0.0, verbose_name='Card Balance')
    status = models.CharField(max_length=150, choices=STATUS_OPTS)


    class Meta:
        unique_together = ('series', 'number')
        ordering = ('-date_created', '-last_used')


    def __str__(self):
        return f'{self.series}-{self.number}'
    

    @property
    def is_active(self):
        return self.status == self.STATUS_OPTS[0][0]
    
    @property
    def is_expired(self):
        return self.status == self.STATUS_OPTS[2][0]

    def deactivate(self):
        self.status = self.STATUS_OPTS[1][0]

    def activate(self):
        self.status = self.STATUS_OPTS[0][0]
    

class Transaction(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    value = models.PositiveIntegerField()

    class Meta:
        ordering = ['-date', '-value']


    def __str__(self):
        return f'{self.value } from {self.card}'