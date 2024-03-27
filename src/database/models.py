from sqlalchemy import Column, Integer, String,Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=True)
    phone = Column(String(10), nullable=True)
    birthday = Column(Date, nullable=False)
    description = Column(String(300), nullable=True)
