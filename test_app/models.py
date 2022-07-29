from django.db import models


class Clients(models.Model):
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'clients'


class Durations(models.Model):
    client = models.ForeignKey('Clients',
                               on_delete=models.CASCADE)
    equipment = models.ForeignKey('Equipment',
                                  on_delete=models.CASCADE)
    start = models.TextField()
    stop = models.TextField()
    mode = models.ForeignKey('Modes',
                             on_delete=models.CASCADE)
    minutes = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'durations'


class Equipment(models.Model):
    client_id = models.IntegerField()
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'equipment'


class Modes(models.Model):
    name = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modes'
