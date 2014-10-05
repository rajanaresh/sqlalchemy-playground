from sqlalchemy import schema, types

metadata = schema.MetaData()

page_table = schema.Table('page', metadata,
                          schema.Column('id', types.Integer, primary_key=True),
                          schema.Column('name', types.Unicode(255), default=u''),
                          schema.Column('title', types.Unicode(255), default=u'Untitled Page'),
                          schema.Column('content', types.Text(), default=u''),
                          )

def printtable(t):
    print("Table name: ", t.name)
    print("t is page_table ", t is page_table)

[printtable(t) for t in metadata.sorted_tables]

def printcolumns(c):
    print("Column: ", c.type)

[printcolumns(c) for c in page_table.columns]

## All types
# String
# Unicode
# Text/UnicodeText
# Numeric
# Float
# Datetime/Date/Time
# Interval
# Binary
# Boolean

from sqlalchemy.engine import create_engine

engine = create_engine('sqlite:///:memory:', echo=True)

metadata.bind = engine

metadata.create_all(checkfirst=True)

