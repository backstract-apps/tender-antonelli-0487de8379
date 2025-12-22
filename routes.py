from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile,Query, Form
from sqlalchemy.orm import Session
from typing import List,Annotated
import service, models, schemas
from fastapi import Query
from database import SessionLocal
from middleware.application_middleware import default_dependency


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.put('/cases/id/')
async def put_cases_id(raw_data: schemas.PutCasesId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_cases_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/users/')
async def post_users(raw_data: schemas.PostUsers, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_users(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/users/id/')
async def put_users_id(raw_data: schemas.PutUsersId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_users_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/clients/id/')
async def put_clients_id(raw_data: schemas.PutClientsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_clients_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/payments/id/')
async def get_payments_id(query: schemas.GetPaymentsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_payments_id(db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/documents/')
async def get_documents(db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_documents(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/payments/')
async def post_payments(raw_data: schemas.PostPayments, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_payments(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/payments/id/')
async def put_payments_id(raw_data: schemas.PutPaymentsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_payments_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/payments/id/')
async def delete_payments_id(query: schemas.DeletePaymentsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_payments_id(db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/cases/')
async def get_cases(db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_cases(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/clients/')
async def post_clients(raw_data: schemas.PostClients, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_clients(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/clients/id/')
async def delete_clients_id(query: schemas.DeleteClientsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_clients_id(db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/payments/')
async def get_payments(db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_payments(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/documents/')
async def post_documents(raw_data: schemas.PostDocuments, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_documents(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/documents/id/')
async def put_documents_id(raw_data: schemas.PutDocumentsId, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.put_documents_id(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/documents/id/')
async def delete_documents_id(query: schemas.DeleteDocumentsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_documents_id(db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/')
async def get_users(db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_users(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/cases/id/')
async def get_cases_id(query: schemas.GetCasesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_cases_id(db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/cases/id/')
async def delete_cases_id(query: schemas.DeleteCasesIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_cases_id(db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/clients/')
async def get_clients(db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_clients(db)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/users/id/')
async def get_users_id(query: schemas.GetUsersIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_users_id(db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/users/id/')
async def delete_users_id(query: schemas.DeleteUsersIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.delete_users_id(db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/clients/id/')
async def get_clients_id(query: schemas.GetClientsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_clients_id(db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/documents/id/')
async def get_documents_id(query: schemas.GetDocumentsIdQueryParams = Depends(), db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.get_documents_id(db, query.id)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/cases/')
async def post_cases(raw_data: schemas.PostCases, db: Session = Depends(get_db), protected_deps_1: dict = Depends(default_dependency)):
    try:
        return await service.post_cases(db, raw_data)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(500, str(e))

