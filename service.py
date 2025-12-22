from sqlalchemy.orm import Session, aliased
from database import SessionLocal
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3
import jwt
from datetime import datetime
import requests
import math
import random
import asyncio
from pathlib import Path


def convert_to_datetime(date_string):
    if date_string is None:
        return datetime.now()
    from fastapi import HTTPException

    if "T" in date_string:
        try:
            return datetime.fromisoformat(date_string.replace("Z", "+00:00"))
        except ValueError:
            date_part = date_string.split("T")[0]
            try:
                return datetime.strptime(date_part, "%Y-%m-%d")
            except ValueError:
                raise HTTPException(
                    status_code=422,
                    detail=f"Improper format in datetime: {date_string}",
                )
    else:
        try:
            return datetime.strptime(date_string, "%Y-%m-%d")
        except ValueError:
            raise HTTPException(
                status_code=422, detail=f"Improper format in datetime: {date_string}"
            )


async def put_cases_id(db: Session, raw_data: schemas.PutCasesId):
    id: int = raw_data.id
    client_id: int = raw_data.client_id
    agent_id: int = raw_data.agent_id
    visa_type: str = raw_data.visa_type
    current_status: str = raw_data.current_status
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Cases)
    query = query.filter(and_(models.Cases.id == id))
    cases_edited_record = query.first()

    if cases_edited_record:
        for key, value in {
            "id": id,
            "agent_id": agent_id,
            "client_id": client_id,
            "visa_type": visa_type,
            "created_at_dt": created_at_dt,
            "current_status": current_status,
        }.items():
            setattr(cases_edited_record, key, value)

        db.commit()
        db.refresh(cases_edited_record)

        cases_edited_record = (
            cases_edited_record.to_dict()
            if hasattr(cases_edited_record, "to_dict")
            else vars(cases_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"cases_edited_record": cases_edited_record},
    }
    return res


async def post_users(db: Session, raw_data: schemas.PostUsers):
    email: str = raw_data.email
    password_hash: str = raw_data.password_hash
    full_name: str = raw_data.full_name
    role: str = raw_data.role
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "role": role,
        "email": email,
        "full_name": full_name,
        "created_at_dt": created_at_dt,
        "password_hash": password_hash,
    }
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    users_inserted_record = new_users.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_inserted_record": users_inserted_record},
    }
    return res


async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id: int = raw_data.id
    email: str = raw_data.email
    password_hash: str = raw_data.password_hash
    full_name: str = raw_data.full_name
    role: str = raw_data.role
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))
    users_edited_record = query.first()

    if users_edited_record:
        for key, value in {
            "id": id,
            "role": role,
            "email": email,
            "full_name": full_name,
            "created_at_dt": created_at_dt,
            "password_hash": password_hash,
        }.items():
            setattr(users_edited_record, key, value)

        db.commit()
        db.refresh(users_edited_record)

        users_edited_record = (
            users_edited_record.to_dict()
            if hasattr(users_edited_record, "to_dict")
            else vars(users_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_edited_record": users_edited_record},
    }
    return res


async def put_clients_id(db: Session, raw_data: schemas.PutClientsId):
    id: int = raw_data.id
    first_name: str = raw_data.first_name
    last_name: str = raw_data.last_name
    passport_number: str = raw_data.passport_number
    nationality: str = raw_data.nationality
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Clients)
    query = query.filter(and_(models.Clients.id == id))
    clients_edited_record = query.first()

    if clients_edited_record:
        for key, value in {
            "id": id,
            "last_name": last_name,
            "first_name": first_name,
            "nationality": nationality,
            "created_at_dt": created_at_dt,
            "passport_number": passport_number,
        }.items():
            setattr(clients_edited_record, key, value)

        db.commit()
        db.refresh(clients_edited_record)

        clients_edited_record = (
            clients_edited_record.to_dict()
            if hasattr(clients_edited_record, "to_dict")
            else vars(clients_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"clients_edited_record": clients_edited_record},
    }
    return res


async def get_payments_id(db: Session, id: int):

    query = db.query(models.Payments)
    query = query.filter(and_(models.Payments.id == id))

    payments_one = query.first()

    payments_one = (
        (
            payments_one.to_dict()
            if hasattr(payments_one, "to_dict")
            else vars(payments_one)
        )
        if payments_one
        else payments_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"payments_one": payments_one},
    }
    return res


async def get_documents(db: Session):

    query = db.query(models.Documents)

    documents_all = query.all()
    documents_all = (
        [new_data.to_dict() for new_data in documents_all]
        if documents_all
        else documents_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"documents_all": documents_all},
    }
    return res


async def post_payments(db: Session, raw_data: schemas.PostPayments):
    case_id: int = raw_data.case_id
    amount: float = raw_data.amount
    fee_type: str = raw_data.fee_type
    is_paid: int = raw_data.is_paid
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "amount": amount,
        "case_id": case_id,
        "is_paid": is_paid,
        "fee_type": fee_type,
        "created_at_dt": created_at_dt,
    }
    new_payments = models.Payments(**record_to_be_added)
    db.add(new_payments)
    db.commit()
    db.refresh(new_payments)
    payments_inserted_record = new_payments.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"payments_inserted_record": payments_inserted_record},
    }
    return res


async def put_payments_id(db: Session, raw_data: schemas.PutPaymentsId):
    id: int = raw_data.id
    case_id: int = raw_data.case_id
    amount: float = raw_data.amount
    fee_type: str = raw_data.fee_type
    is_paid: int = raw_data.is_paid
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Payments)
    query = query.filter(and_(models.Payments.id == id))
    payments_edited_record = query.first()

    if payments_edited_record:
        for key, value in {
            "id": id,
            "amount": amount,
            "case_id": case_id,
            "is_paid": is_paid,
            "fee_type": fee_type,
            "created_at_dt": created_at_dt,
        }.items():
            setattr(payments_edited_record, key, value)

        db.commit()
        db.refresh(payments_edited_record)

        payments_edited_record = (
            payments_edited_record.to_dict()
            if hasattr(payments_edited_record, "to_dict")
            else vars(payments_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"payments_edited_record": payments_edited_record},
    }
    return res


async def delete_payments_id(db: Session, id: int):

    query = db.query(models.Payments)
    query = query.filter(and_(models.Payments.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        payments_deleted = record_to_delete.to_dict()
    else:
        payments_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"payments_deleted": payments_deleted},
    }
    return res


async def get_cases(db: Session):

    query = db.query(models.Cases)

    cases_all = query.all()
    cases_all = (
        [new_data.to_dict() for new_data in cases_all] if cases_all else cases_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"cases_all": cases_all},
    }
    return res


async def post_clients(db: Session, raw_data: schemas.PostClients):
    first_name: str = raw_data.first_name
    last_name: str = raw_data.last_name
    passport_number: str = raw_data.passport_number
    nationality: str = raw_data.nationality
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "last_name": last_name,
        "first_name": first_name,
        "nationality": nationality,
        "created_at_dt": created_at_dt,
        "passport_number": passport_number,
    }
    new_clients = models.Clients(**record_to_be_added)
    db.add(new_clients)
    db.commit()
    db.refresh(new_clients)
    clients_inserted_record = new_clients.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"clients_inserted_record": clients_inserted_record},
    }
    return res


async def delete_clients_id(db: Session, id: int):

    query = db.query(models.Clients)
    query = query.filter(and_(models.Clients.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        clients_deleted = record_to_delete.to_dict()
    else:
        clients_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"clients_deleted": clients_deleted},
    }
    return res


async def get_payments(db: Session):

    query = db.query(models.Payments)

    payments_all = query.all()
    payments_all = (
        [new_data.to_dict() for new_data in payments_all]
        if payments_all
        else payments_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"payments_all": payments_all},
    }
    return res


async def post_documents(db: Session, raw_data: schemas.PostDocuments):
    case_id: int = raw_data.case_id
    document_type: str = raw_data.document_type
    file_path: str = raw_data.file_path
    is_validated: int = raw_data.is_validated
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "case_id": case_id,
        "file_path": file_path,
        "is_validated": is_validated,
        "created_at_dt": created_at_dt,
        "document_type": document_type,
    }
    new_documents = models.Documents(**record_to_be_added)
    db.add(new_documents)
    db.commit()
    db.refresh(new_documents)
    documents_inserted_record = new_documents.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"documents_inserted_record": documents_inserted_record},
    }
    return res


async def put_documents_id(db: Session, raw_data: schemas.PutDocumentsId):
    id: int = raw_data.id
    case_id: int = raw_data.case_id
    document_type: str = raw_data.document_type
    file_path: str = raw_data.file_path
    is_validated: int = raw_data.is_validated
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    query = db.query(models.Documents)
    query = query.filter(and_(models.Documents.id == id))
    documents_edited_record = query.first()

    if documents_edited_record:
        for key, value in {
            "id": id,
            "case_id": case_id,
            "file_path": file_path,
            "is_validated": is_validated,
            "created_at_dt": created_at_dt,
            "document_type": document_type,
        }.items():
            setattr(documents_edited_record, key, value)

        db.commit()
        db.refresh(documents_edited_record)

        documents_edited_record = (
            documents_edited_record.to_dict()
            if hasattr(documents_edited_record, "to_dict")
            else vars(documents_edited_record)
        )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"documents_edited_record": documents_edited_record},
    }
    return res


async def delete_documents_id(db: Session, id: int):

    query = db.query(models.Documents)
    query = query.filter(and_(models.Documents.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        documents_deleted = record_to_delete.to_dict()
    else:
        documents_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"documents_deleted": documents_deleted},
    }
    return res


async def get_users(db: Session):

    query = db.query(models.Users)

    users_all = query.all()
    users_all = (
        [new_data.to_dict() for new_data in users_all] if users_all else users_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_all": users_all},
    }
    return res


async def get_cases_id(db: Session, id: int):

    query = db.query(models.Cases)
    query = query.filter(and_(models.Cases.id == id))

    cases_one = query.first()

    cases_one = (
        (cases_one.to_dict() if hasattr(cases_one, "to_dict") else vars(cases_one))
        if cases_one
        else cases_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"cases_one": cases_one},
    }
    return res


async def delete_cases_id(db: Session, id: int):

    query = db.query(models.Cases)
    query = query.filter(and_(models.Cases.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        cases_deleted = record_to_delete.to_dict()
    else:
        cases_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"cases_deleted": cases_deleted},
    }
    return res


async def get_clients(db: Session):

    query = db.query(models.Clients)

    clients_all = query.all()
    clients_all = (
        [new_data.to_dict() for new_data in clients_all] if clients_all else clients_all
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"clients_all": clients_all},
    }
    return res


async def get_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    users_one = query.first()

    users_one = (
        (users_one.to_dict() if hasattr(users_one, "to_dict") else vars(users_one))
        if users_one
        else users_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_one": users_one},
    }
    return res


async def delete_users_id(db: Session, id: int):

    query = db.query(models.Users)
    query = query.filter(and_(models.Users.id == id))

    record_to_delete = query.first()
    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete.to_dict()
    else:
        users_deleted = record_to_delete

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"users_deleted": users_deleted},
    }
    return res


async def get_clients_id(db: Session, id: int):

    query = db.query(models.Clients)
    query = query.filter(and_(models.Clients.id == id))

    clients_one = query.first()

    clients_one = (
        (
            clients_one.to_dict()
            if hasattr(clients_one, "to_dict")
            else vars(clients_one)
        )
        if clients_one
        else clients_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"clients_one": clients_one},
    }
    return res


async def get_documents_id(db: Session, id: int):

    query = db.query(models.Documents)
    query = query.filter(and_(models.Documents.id == id))

    documents_one = query.first()

    documents_one = (
        (
            documents_one.to_dict()
            if hasattr(documents_one, "to_dict")
            else vars(documents_one)
        )
        if documents_one
        else documents_one
    )

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"documents_one": documents_one},
    }
    return res


async def post_cases(db: Session, raw_data: schemas.PostCases):
    client_id: int = raw_data.client_id
    agent_id: int = raw_data.agent_id
    visa_type: str = raw_data.visa_type
    current_status: str = raw_data.current_status
    created_at_dt: str = convert_to_datetime(raw_data.created_at_dt)

    record_to_be_added = {
        "agent_id": agent_id,
        "client_id": client_id,
        "visa_type": visa_type,
        "created_at_dt": created_at_dt,
        "current_status": current_status,
    }
    new_cases = models.Cases(**record_to_be_added)
    db.add(new_cases)
    db.commit()
    db.refresh(new_cases)
    cases_inserted_record = new_cases.to_dict()

    res = {
        "status": 200,
        "message": "This is the default message.",
        "data": {"cases_inserted_record": cases_inserted_record},
    }
    return res
