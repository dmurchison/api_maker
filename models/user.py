import datetime
from models.base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, UniqueConstraint



class User(Base):
    __tablename__ = "user"

    __table_args__ = (UniqueConstraint("username", name="username_unique"), )

    id = Column(Integer, primary_key=True)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    username = Column(String(25), unique=True)
    short_bio = Column(String(50))
    long_bio = Column(String(500))
    # email, password = Column(String(50)), Column(String(50))


