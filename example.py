import asyncio
from pyasyncorm.model import Model, Column
from pyasyncorm.connection import Connection

class User(Model):
  id = Column('int', primary_key=True)
  email = Column('text', unique=True)
  password = Column('text')

class Post(Model):
  id = Column('int', primary_key=True)
  title = Column('text', unique=True)
  body = Column('text')

async def main():
  conn = Connection()
  await conn.connect('pg', 'postgresql://postgres:password@localhost:5432/postgres')
  await conn.migrate([ User ])

  async with conn.transaction():
    u = User(email="hello@world.com")
    print(u)

asyncio.run(main())
