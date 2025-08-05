from .database import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Float, text
from sqlalchemy.orm import relationship




class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key= True, nullable= False)
    user_id = Column(Integer, ForeignKey("users.id"),nullable= False)
    status = Column(String, nullable= False)
    gender = Column(String, nullable= False)
    created_at = Column(TIMESTAMP(timezone= True), nullable= False, server_default= text('now()'))
    returned_at = Column(TIMESTAMP(timezone= True))
    shipped_at = Column(TIMESTAMP(timezone= True))
    delivered_at = Column(TIMESTAMP(timezone= True))
    num_of_item = Column(Integer, nullable= False)
    user = relationship("User", back_populates="orders")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True, index= True,nullable= False)
    first_name = Column(String, nullable= False)
    last_name = Column(String, nullable= False)
    email = Column(String, nullable= False, unique= True)
    age = Column(Integer, nullable= False)
    gender = Column(String, nullable= False)
    state = Column(String, nullable= False)
    street_address = Column(String, nullable= False)
    postal_code = Column(String, nullable= False) 
    city = Column(String, nullable= False)
    country = Column(String, nullable= False)
    latitude = Column(Float, nullable= False)
    longitude = Column(Float, nullable= False)
    traffic_source = Column(String, nullable= False)
    created_at = Column(TIMESTAMP(timezone= True), nullable= False, server_default= text('now()'))
    orders = relationship("Order", back_populates="user")

