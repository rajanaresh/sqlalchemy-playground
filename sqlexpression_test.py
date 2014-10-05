from metadata_test import engine, page_table

print("\nSQL Expression Example\n")

connection = engine.connect()

# tablename.insert(dict())

ins = page_table.insert(
    values=dict(name=u'test', title=u'Test Page', content=u'Some Content!')
    )

print(ins)

result = connection.execute(ins)
print(result)

print("\nSelecting Results\n")

from sqlalchemy.sql import select

# select([tablename], whereclause).order_by(coloumname.desc())

s = select([page_table])
result = connection.execute(s)
[print(row) for row in result]

s = select([page_table], page_table.columns.id==1)
result = connection.execute(s)
print(result.fetchall())

from sqlalchemy.sql import and_, or_, not_

s = select([page_table], and_(page_table.c.id<=10, page_table.c.name.like(u't%'))).order_by(page_table.c.title.desc(), page_table.c.id)


result = connection.execute(s)
print(result.fetchall())

print("\nUpdating Results\n")

from sqlalchemy import update

# update(tablename, which rows to update)
# connection.execute(updateobject, columnname=new value)

u = update(page_table, page_table.c.title==u'New Title')
connection.execute(u, title=u"Updated Title")

print("\nDeleting Row\n")

from sqlalchemy import delete

# delete(tablename, which rows to delete)
# connection.execute(deleteobject)

d = delete(page_table, page_table.c.id==1)
connection.execute(d)

connection.close()


