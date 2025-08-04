from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class OrderBase(BaseModel):
    id: int
    order_id: int
    user_id: int
    status: str
    gender: str
    created_at: Optional[datetime] = None 
    returned_at: Optional[datetime] = None
    shipped_at: Optional[datetime] = None
    delivered_at: Optional[datetime] = None
    num_of_item: int = Field(..., gt=0)

class OrderCreate(OrderBase):
    pass

# Response Models
class Order(BaseModel):
    order_id: int
    user_id: int
    status: str
    gender: str
    created_at: datetime 
    returned_at: datetime
    shipped_at: datetime
    delivered_at: datetime
    num_of_item: int = Field(..., gt=0)

    model_config = {
        "from_attributes": True
    }

# User Schemas

class UserBase(BaseModel):
    id :int
    firstnamme :str
    lastnamme :str
    email : EmailStr
    age :int
    gender : str
    state :str
    street_address : str
    postal_code :int 
    city :str
    country :str
    lattitude : str
    longitude :str
    traffic_source :str
    created_at = datetime

class UserOut(BaseModel):
    id :int
    firstnamme :str
    lastnamme :str
    email : EmailStr
    age :int
    gender : str
    state :str
    street_address : str
    postal_code :int 
    city :str
    country :str
    lattitude : str
    longitude :str
    traffic_source :str
    created_at = datetime

    model_config = {
        "from_attributes": True
    }
