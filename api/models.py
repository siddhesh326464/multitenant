from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime,timezone
from utils.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    domain = Column(String,unique=True, index=True , nullable=True)
    is_active = Column(Boolean, default=True)
    account = relationship("Account",back_populates='project')

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    first_name = Column(String,nullable=True)
    last_name = Column(String,nullable=True)
    email = Column(String, unique=True, index=True)
    contact = Column(String,nullable=True)
    is_active = Column(Boolean,default=True)
    project_id = Column(Integer,ForeignKey("projects.id",ondelete='CASCADE'))
    project = relationship("Project",back_populates='account')
