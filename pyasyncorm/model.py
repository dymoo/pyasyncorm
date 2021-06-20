import json

class Column:
  def __init__(self, col_type, primary_key=False, unique=False, not_null=True, default=''):
    self.type = col_type
    self.primary_key = primary_key
    self.unique = unique
    self.not_null = not_null
    self.default = default

class Model:
  @property
  def attribs(self):
    return (getattr(self, 'model_name'),\
      getattr(self, 'col_defs'))

  def __repr__(self):
    (name, cols) = self.attribs
    return f'Model; name: {name}; contents: {json.dumps(cols)}'

  def __init__(self, **kwargs):
    print('__init__ called with', kwargs)

    c  = self.__class__
    setattr(self, 'model_name', c.__name__)
    setattr(self, 'col_defs', {})

    for col_name in c.__dict__:
      col = c.__dict__[col_name]
      if isinstance(col, Column):
        for col_def in col.__dict__:
          setattr(self, col_name, kwargs[col_name] if col_name in kwargs else col_def['default'])
          setattr(self, 'col_defs.' + col_name, col_def)

  async def new(self, conn, **kwargs):
    pass

  async def findOne(self, conn, **kwargs):
    pass

  async def find(self, conn, **kwargs):
    pass

  async def updateOne(self, conn, **kwargs):
    pass

  async def update(self, conn, **kwargs):
    pass

  async def save(self, conn, **kwargs):
    pass
  