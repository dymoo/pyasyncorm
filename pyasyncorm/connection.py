import asyncpg

class Connection:
  db = None
  conn = None

  @property
  def connected(self):
    return bool(self.conn)

  @property
  def transaction(self):
    if self.db == 'pg':
      return self.conn.transaction

  async def connect(self, db, *args, **kwargs):
    if db in ('pg', 'postgres', 'postgresql'):
      self.db = 'pg'
      self.conn = await asyncpg.connect(*args, **kwargs)
    else:
      raise ValueError('Unknown connector')

  async def query(self, sql, **kwargs):
    if self.db == 'pg':
      return await self.conn.fetch(sql, **kwargs)

  async def close(self):
    if self.db == 'pg':
      await self.conn.close()

  async def migrate(self, models):
    for model in models:
      (name, cols) = model().attribs
      sql = f"CREATE TABLE IF NOT EXISTS public.{name} (\n"
      for (col_idx, (col_name, col_def)) in enumerate(cols):
        sql += f"{col_name} {col_def['type']}"
        if col_def['primary_key']:
          sql += " PRIMARY KEY"
        if col_def['unique']:
          sql += " UNIQUE"
        if col_def['not_null']:
          sql += " NOT NULL"
        sql += ("\n" if (len(cols) - 1 == col_idx) else ",\n")
      sql += ");"
      await self.query(sql)
