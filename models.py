from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Boolean
)
from datetime import datetime

Base = declarative_base()


class Event(Base):
    __tablename__ = 'Event'

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, name='eventId')
    title = Column(String(256))
    min_price = Column(Float, name='minPrice')
    max_price = Column(Float, name='maxPrice')
    ticket_count = Column(Integer, name='ticketCount')
    begin_date = Column(DateTime, name='beginDate')
    end_date = Column(DateTime, name='endDate')
    poster_image_url = Column(String(256), name='posterImageURL')
    sales_stopped = Column(Boolean, name='salesStopped')
    ended = Column(Boolean, name='ended')
    revision = Column(Integer)

    def __init__(self,
                 event_id: int,
                 title: str,
                 min_price: float,
                 max_price: float,
                 ticket_count: int,
                 begin_date: datetime,
                 end_date: datetime,
                 poster_image_url: str,
                 sales_stopped: bool,
                 ended: bool,
                 revision: int):
        self.event_id = event_id
        self.title = title
        self.min_price = float(min_price)
        self.max_price = float(max_price)
        self.ticket_count = ticket_count
        self.begin_date = begin_date
        self.end_date = end_date
        self.poster_image_url = poster_image_url
        self.sales_stopped = sales_stopped
        self.ended = ended
        self.revision = revision
