from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import mapper

DB_USER = 'study'
DB_PASSWORD = 'study'
DB_NAME = 'study'
DB_ECHO = True
group_table = create_engine(
    f'postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}',
    echo=True,
)
if not database_exists(engine.url):
    create_database(engine.url)

metadata = MetaData()
users_table = Table('Group', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    )
metadata.create_all(engine)


class Group:
    def __init__(self, name):
        self.name = name


mapper(Group, group_table)
