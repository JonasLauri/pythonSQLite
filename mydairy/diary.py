#!/usr/bin/env python
import datetime
from peewee import *

# init sqlite database
db = SqliteDatabase('diary.db')

# create database model
class BaseModel(Model):
    class Meta:
        database = db # init diary.db

class Entry(BaseModel):
    # table fields
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

# create database and table if they dont exist
def initialize():
    db.connect()
    db.create_tables([Entry], safe=True)


def menu_loop():
    """Show the menu"""

def add_entry():
    """Add an entry"""

def view_entries():
    """View previous entries"""

def delete_entry():
    """Delete an entry"""


# script run 
if __name__ == '__main__':
    initialize()
    menu_loop()
