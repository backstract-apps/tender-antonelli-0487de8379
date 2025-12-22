

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
     "sqlite+libsql:///embedded.db",
     connect_args={
         "sync_url": "libsql://coll-8295bcdaf4ec40f897d5b3e2887e991f-mayson.aws-ap-south-1.turso.io",
         "auth_token": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NjY0MjU3MTEsInAiOnsicm9hIjp7Im5zIjpbIjUyMjM2NWU0LTBmNzItNGI0Yi04YjZhLTkzMTc4ZjEzNzBhZSJdfSwicnciOnsibnMiOlsiNTIyMzY1ZTQtMGY3Mi00YjRiLThiNmEtOTMxNzhmMTM3MGFlIl19fSwicmlkIjoiM2U5NzBhYjctNzI0Yy00YzVjLWI1NmEtOGFjYjFkZTRhOGM2In0.JkNEb3qP7dXqFkCvs4kYyu79QtZueJO-kQlaTadI3Caab3fJnmzs69wGG0n9I9Ib7t1S4vQHgTdrGlPJuZUyCg",
     },
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

