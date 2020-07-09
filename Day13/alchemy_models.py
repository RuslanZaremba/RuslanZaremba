from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper

engine = create_engine("sqlite:///test1.db", echo=True)
metadata = MetaData()
users_table = Table('user', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('firstname', String),
                    Column('lastname', String)
                    )
metadata.create_all(engine)


class User:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):

        return f"{self.firstname} {self.lastname}"


mapper(User, users_table)
user = User('Ruslan', 'Zaremba')
user1 = User('olga', 'zaremba')
user2 = User('tanya', 'zaremba')

Session = sessionmaker(bind=engine)
session = Session()
# session.add(user)
# session.add(user1)
# session.add(user2)
# session.commit()


person = session.query(User).filter_by(firstname="Ruslan").first()
print(person)
