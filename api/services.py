from fastapi import HTTPException
from api.models import Project,Account
from sqlalchemy.orm.session import Session

def create_user(project,userdata,db : Session):
    project_obj = db.query(Project).filter(Project.domain == project,Project.is_active == True).first()
    if not project_obj:
        raise HTTPException(status_code=404,detail="Project not present for this domain")
    user_data = Account(
        first_name  = userdata.first_name,
        last_name = userdata.last_name,
        email = userdata.email,
        contact = userdata.contact,
        is_active = userdata.is_active,
        project_id = project_obj.id
    )
    db.add(user_data)
    db.commit()
    db.refresh(user_data)
    return user_data


def get_user_list(project,db:Session):
    project_obj = db.query(Project).filter(Project.domain == project,Project.is_active == True).first()
    if not project_obj:
        raise HTTPException(status_code=404,detail="Project not present for this domain")
    user_list = db.query(Account).filter(Account.project_id == project_obj.id,Account.is_active == True).all()
    return user_list

def user_detail(project,user_id,db:Session):
    project_obj = db.query(Project).filter(Project.domain == project,Project.is_active == True).first()
    if not project_obj:
        raise HTTPException(status_code=404,detail="Project not present for this domain")  
    user_obj = db.query(Account).filter(Account.id == user_id , Account.is_active == True, Account.project_id == project_obj.id).first()
    if not user_obj:
        raise HTTPException(status_code=404,detail="user not found")
    return user_obj


def update_detail(project,user_id,user_data,db:Session):
    project_obj = db.query(Project).filter(Project.domain == project,Project.is_active == True).first()
    if not project_obj:
        raise HTTPException(status_code=404,detail="Project not present for this domain")
    user_obj = db.query(Account).filter(Account.id == user_id , Account.is_active == True, Account.project_id == project_obj.id).first()
    if not user_obj:
        raise HTTPException(status_code=404,detail="user not found")
    user_obj.first_name = user_data.first_name
    user_obj.last_name = user_data.last_name
    user_obj.email = user_data.email
    user_obj.contact = user_data.contact
    user_obj.is_active = user_data.is_active
    db.commit()
    db.refresh(user_obj)
    return user_obj
    
def tenent_delete_user(project,user_id,db:Session):
    project_obj = db.query(Project).filter(Project.domain == project,Project.is_active == True).first()
    if not project_obj:
        raise HTTPException(status_code=404,detail="Project not present for this domain")
    user_obj = db.query(Account).filter(Account.id == user_id , Account.is_active == True, Account.project_id == project_obj.id).first()
    if not user_obj:
        raise HTTPException(status_code=404,detail="user not found")
    db.delete(user_obj)
    db.commit()
    return {"message": "Item deleted successfully"}