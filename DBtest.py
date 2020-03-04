from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_migrate import Migrate
from flask_moment import Moment
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

Base = declarative_base()

dbtest = Flask(__name__)
moment = Moment(dbtest)
dbtest.config.from_object('config')
db = SQLAlchemy(dbtest)

migrate = Migrate(dbtest,db)


association_table = Table('association', Base.metadata,
    Column('left_id', Integer, ForeignKey('left.id')),
    Column('right_id', Integer, ForeignKey('right.id'))
)

class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Child",
                    secondary=association_table,
                    backref="parents")

class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)