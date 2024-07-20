from fastapi import APIRouter,Depends,Request
from sqlalchemy.orm.session import Session
from utils.database import get_db
from api import services as account_services
from api.schema import CretaeUser,GetUsers,UpdateUser

account_router = APIRouter()


@account_router.post('/add_users')
async def create_user(project:str,user_data:CretaeUser,db:Session = Depends(get_db)):
    """
    create user
    """
    user_obj =account_services.create_user(project,user_data,db = db)
    return user_obj

@account_router.get('/get_users',response_model=list[GetUsers])
async def get_users(project:str,db:Session = Depends(get_db)):
    """
    get all user of this project 
    """
    userlist = account_services.get_user_list(project,db = db)
    return userlist

@account_router.get('/userdetail',response_model=GetUsers)
async def user_details(project:str,user_id:int,db:Session = Depends(get_db)):
    """
    get detail of the perticular user
    """
    userdetail = account_services.user_detail(project,user_id,db = db)
    return userdetail

@account_router.put('/update_users/{user_id}/')
async def update_detail(project:str,user_id:int,data:UpdateUser,db:Session = Depends(get_db)):
    """
    update details of the perticular user
    """
    updated_user = account_services.update_detail(project,user_id,data,db = db)
    return updated_user

@account_router.put('/delete_users/{user_id}/')
def delete_user(project:str,user_id:int,db:Session = Depends(get_db)):
    """
    delete user this is the hard delete
    """
    user_object = account_services.tenent_delete_user(project,user_id,db=db)
    return user_object


