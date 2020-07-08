from sqlalchemy import create_engine

e = create_engine("sqlite:///address_oblast.db")
find = e.execute("""select * from address_oblast""")
for i in find:
