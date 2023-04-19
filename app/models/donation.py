from sqlalchemy import Column, ForeignKey, Integer, Text

from .abstract import Abstract


class Donation(Abstract):
    '''Модель пожертвований таблицы donation.'''
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
