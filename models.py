import config
import peewee


class Book(peewee.Model):
    title = peewee.CharField()

    class Meta:
        database = config.DB
