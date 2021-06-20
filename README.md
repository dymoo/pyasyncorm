# pyasyncorm

Async ORM for postgres with a focus on simplicity, stability and performance.

## Current database support

- PostgreSQL, via asyncpg connector.

## Example code

```python
import asyncio
from pyasyncorm.model import Model, Column
from pyasyncorm.connection import Connection

class User(Model):
  id = Column('int', primary_key=True)
  email = Column('text', unique=True)
  password = Column('text')

async def main():
  # Connect and make sure all our models are migrated.
  conn = Connection()
  await conn.connect('postgresql://')
  await conn.migrate([ User ])

  # Create user
  await User(email='test@mail.com', password='securepassword123').save()

asyncio.run(main())
```
