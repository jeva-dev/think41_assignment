from .database import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean, text




class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key= True, nullable= False)
    order_id = Column(String, nullable= False)
    user_id = Column(String, nullable= False)
    status = Column(String, nullable= False)
    gender = Column(String, nullable= False)
    created_at = Column(TIMESTAMP(timezone= True), nullable= False, server_default= text('now()'))
    returned_at = Column(TIMESTAMP(timezone= True))
    shipped_at = Column(TIMESTAMP(timezone= True))
    delivered_at = Column(TIMESTAMP(timezone= True))
    num_of_item = Column(Integer, nullable= False)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True, nullable= False)
    firstnamme = Column(String, nullable= False)
    lastnamme = Column(String, nullable= False)
    email = Column(String, nullable= False, unique= True)
    age = Column(Integer, nullable= False)
    gender = Column(String, nullable= False)
    state = Column(String, nullable= False)
    street_address = Column(String, nullable= False)
    postal_code = Column(Integer, nullable= False) 
    city = Column(String, nullable= False)
    country = Column(String, nullable= False)
    lattitude = Column(String, nullable= False)
    longitude = Column(String, nullable= False)
    traffic_source = Column(String, nullable= False)
    created_at = Column(TIMESTAMP(timezone= True), nullable= False, server_default= text('now()'))

