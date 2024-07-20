from pydantic import BaseModel,field_validator
import re

class CretaeUser(BaseModel):
    first_name:str
    last_name:str
    email:str
    contact:str
    is_active:bool

    @field_validator('email')
    def check_email(cls,values):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, values):
            raise ValueError("Invalid email address")
        return values
    
    @field_validator('contact')
    def check_contact(cls,value):
        contact_regex = r'^[789]\d{9}$'  
        if not re.match(contact_regex, value):
            raise ValueError("Invalid contact number")
        return value
    
class GetUsers(BaseModel):
    id:int
    first_name:str
    last_name:str
    email:str
    contact:str
    is_active:bool

class UpdateUser(BaseModel):
    first_name:str
    last_name:str
    email:str
    contact:str
    is_active:bool

    @field_validator('email')
    def check_email(cls,values):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, values):
            raise ValueError("Invalid email address")
        return values
    
    @field_validator('contact')
    def check_contact(cls,value):
        contact_regex = r'^[789]\d{9}$'  
        if not re.match(contact_regex, value):
            raise ValueError("Invalid contact number")
        return value