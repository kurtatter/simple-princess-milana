from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    Boolean
)

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
