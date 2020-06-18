from peewee import *
from data import users_info

# database connection 
db = SqliteDatabase('users.db')

# creating new model/table
class User(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    class Meta:
        database = db

# adding dataset to user table
def add_users():
    for user, point in users_info:
        # updates existing rows
        try:
            User.create(username=user, points=point)
        except IntegrityError:
            user_record = User.get(username=user)
            user_record.points = point
            user_record.save()

# ordering by pointsp
def richest_user():
    user = User.select().order_by(User.points.desc()).get()
    return user.username


# script run
if __name__ == '__main__':
    db.connect()
    db.create_tables([User], safe=True)
    add_users()
    print(f"Richest user is : {richest_user()}") 