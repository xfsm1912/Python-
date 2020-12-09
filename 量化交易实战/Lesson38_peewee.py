import peewee
from peewee import *

# db = MySQLDatabase('mysql', user='root', passwd='123456')
# need to add the host and port
db = MySQLDatabase(
    database='mysql',
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='123456'
)


class Price(peewee.Model):
    timestamp = peewee.DateTimeField(primary_key=True)
    BTCUSD = peewee.FloatField()

    class Meta:
        database = db


def test_peewee():
    Price.create_table()
    price = Price(timestamp='2019-06-07 13:17:18', BTCUSD='12345.67')
    price.save()


if __name__ == '__main__':
    test_peewee()
