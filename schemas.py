from pydantic import BaseModel,Field,field_validator

import datetime

import uuid

from typing import Any, Dict, List,Optional,Tuple

import re

class Users(BaseModel):
    email: Optional[str]=None
    password_hash: Optional[str]=None
    full_name: Optional[str]=None
    role: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadUsers(BaseModel):
    email: Optional[str]=None
    password_hash: Optional[str]=None
    full_name: Optional[str]=None
    role: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Clients(BaseModel):
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    passport_number: Optional[str]=None
    nationality: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadClients(BaseModel):
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    passport_number: Optional[str]=None
    nationality: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Cases(BaseModel):
    client_id: Optional[int]=None
    agent_id: Optional[int]=None
    visa_type: Optional[str]=None
    current_status: Optional[str]=None
    created_at_dt: Optional[Any]=None


class ReadCases(BaseModel):
    client_id: Optional[int]=None
    agent_id: Optional[int]=None
    visa_type: Optional[str]=None
    current_status: Optional[str]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Documents(BaseModel):
    case_id: Optional[int]=None
    document_type: Optional[str]=None
    file_path: Optional[str]=None
    is_validated: Optional[int]=None
    created_at_dt: Optional[Any]=None


class ReadDocuments(BaseModel):
    case_id: Optional[int]=None
    document_type: Optional[str]=None
    file_path: Optional[str]=None
    is_validated: Optional[int]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True


class Payments(BaseModel):
    case_id: Optional[int]=None
    amount: Optional[float]=None
    fee_type: Optional[str]=None
    is_paid: Optional[int]=None
    created_at_dt: Optional[Any]=None


class ReadPayments(BaseModel):
    case_id: Optional[int]=None
    amount: Optional[float]=None
    fee_type: Optional[str]=None
    is_paid: Optional[int]=None
    created_at_dt: Optional[Any]=None
    class Config:
        from_attributes = True




class PutCasesId(BaseModel):
    id: int = Field(...)
    client_id: Optional[int]=None
    agent_id: Optional[int]=None
    visa_type: Optional[str]=None
    current_status: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostUsers(BaseModel):
    email: Optional[str]=None
    password_hash: Optional[str]=None
    full_name: Optional[str]=None
    role: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutUsersId(BaseModel):
    id: int = Field(...)
    email: Optional[str]=None
    password_hash: Optional[str]=None
    full_name: Optional[str]=None
    role: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutClientsId(BaseModel):
    id: int = Field(...)
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    passport_number: Optional[str]=None
    nationality: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostPayments(BaseModel):
    case_id: Optional[int]=None
    amount: Optional[Any]=None
    fee_type: Optional[str]=None
    is_paid: Optional[int]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutPaymentsId(BaseModel):
    id: int = Field(...)
    case_id: Optional[int]=None
    amount: Optional[Any]=None
    fee_type: Optional[str]=None
    is_paid: Optional[int]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostClients(BaseModel):
    first_name: Optional[str]=None
    last_name: Optional[str]=None
    passport_number: Optional[str]=None
    nationality: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostDocuments(BaseModel):
    case_id: Optional[int]=None
    document_type: Optional[str]=None
    file_path: Optional[str]=None
    is_validated: Optional[int]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PutDocumentsId(BaseModel):
    id: int = Field(...)
    case_id: Optional[int]=None
    document_type: Optional[str]=None
    file_path: Optional[str]=None
    is_validated: Optional[int]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



class PostCases(BaseModel):
    client_id: Optional[int]=None
    agent_id: Optional[int]=None
    visa_type: Optional[str]=None
    current_status: Optional[str]=None
    created_at_dt: Optional[str]=None

    class Config:
        from_attributes = True



# Query Parameter Validation Schemas

class GetPaymentsIdQueryParams(BaseModel):
    """Query parameter validation for get_payments_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeletePaymentsIdQueryParams(BaseModel):
    """Query parameter validation for delete_payments_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteClientsIdQueryParams(BaseModel):
    """Query parameter validation for delete_clients_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteDocumentsIdQueryParams(BaseModel):
    """Query parameter validation for delete_documents_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetCasesIdQueryParams(BaseModel):
    """Query parameter validation for get_cases_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteCasesIdQueryParams(BaseModel):
    """Query parameter validation for delete_cases_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetUsersIdQueryParams(BaseModel):
    """Query parameter validation for get_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class DeleteUsersIdQueryParams(BaseModel):
    """Query parameter validation for delete_users_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetClientsIdQueryParams(BaseModel):
    """Query parameter validation for get_clients_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True


class GetDocumentsIdQueryParams(BaseModel):
    """Query parameter validation for get_documents_id"""
    id: int = Field(..., ge=1, description="Id")

    class Config:
        populate_by_name = True
