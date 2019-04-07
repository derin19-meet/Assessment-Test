from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_applicant(id, name, age, subject):
  new_applicant = Applicant(
    id=id,
    name=name,
    age=age,
    subject=subject)
  session.add(new_applicant)
  session.commit()

def get_all_applicants():
    applicants = session.query(Applicant).all()
    return applicants


def save_to_database():
