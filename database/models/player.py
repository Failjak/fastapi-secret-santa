from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref

from ..base_class import Base


class Player(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String)
    social_url = Column(String, nullable=False)
    santa_id = Column(Integer, ForeignKey("secretsanta.id"))

    user_id = Column(Integer, ForeignKey("user.id"), nullable=True)
    user = relationship("User", backref=backref("player", uselist=False))
