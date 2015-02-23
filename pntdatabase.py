from peewee import * 
db = SqliteDatabase ('pewee.db')


class User(Model):
	name = TextField()
	email = TextField()
	password = TextField()
	username = TextField()

class Pin(Model): 
	title = TextField()
	url = TextField()
	description = TextField()
	user = ForeignKeyField(User, related_name = "pins")

#db.create_tables([User, Pin])

def create_user(name, email, password, username):
	newuser= User(name=name, email=email, password=password, username=username)
	newuser.save()

name = raw_input ("what is your name? ")
email = raw_input ("Your email ")
password = raw_input ("What is your password?")
username = raw_input ("Please pick a username ") 

create_user (name, email, password, username) 
print "Account created!"



