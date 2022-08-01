from django.db import models
from django.db.models.query import QuerySet


class DBQuerySet(QuerySet):
    """Create class for filtering."""

    def db_query(self, instance):
        return self.filter(
            client=instance.client,
            equipment=instance.equipment,
            mode=instance.mode,
            minutes=instance.minutes,
            start__year=instance.start.date().year,
            stop__year=instance.stop.date().year,
            start__month=instance.start.date().month,
            stop__month=instance.stop.date().month,
            start__day=instance.start.date().day,
            stop__day=instance.stop.date().day,
            start__hour=instance.start.time().hour,
            stop__hour=instance.stop.time().hour,
        )

    def db_query_without_hour(self, instance):
        return self.filter(
            client=instance.client,
            equipment=instance.equipment,
            mode=instance.mode,
            minutes=instance.minutes,
            start__year=instance.start.date().year,
            stop__year=instance.stop.date().year,
            start__month=instance.start.date().month,
            stop__month=instance.stop.date().month,
            start__day=instance.start.date().day,
            stop__day=instance.stop.date().day,
        )

    def db_query_without_day(self, instance):
        return self.filter(
            client=instance.client,
            equipment=instance.equipment,
            mode=instance.mode,
            minutes=instance.minutes,
            start__year=instance.start.date().year,
            stop__year=instance.stop.date().year,
            start__month=instance.start.date().month,
            stop__month=instance.stop.date().month,
        )

    def db_query_without_month(self, instance):
        return self.filter(
            client=instance.client,
            equipment=instance.equipment,
            mode=instance.mode,
            minutes=instance.minutes,
            start__year=instance.start.date().year,
            stop__year=instance.stop.date().year,
        )

    def db_query_without_year(self, instance):
        return self.filter(
            client=instance.client,
            equipment=instance.equipment,
            mode=instance.mode,
            minutes=instance.minutes,
        )


class DBManager(models.Manager):
    """Class for models, overrides base model.Manager()."""

    def get_queryset(self):
        return DBQuerySet(self.model, using=self._db)

    def db_query(self, instance):
        return self.get_queryset().db_query(instance)

    def db_query_without_hour(self, instance):
        return self.get_queryset().db_query_without_day(instance)

    def db_query_without_day(self, instance):
        return self.get_queryset().db_query_without_hour(instance)

    def db_query_without_month(self, instance):
        return self.get_queryset().db_query_without_hour(instance)

    def db_query_without_year(self, instance):
        return self.get_queryset().db_query_without_hour(instance)
