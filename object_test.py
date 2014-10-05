from model import Page, Comment, Tag, Base, session
from sqlalchemy import orm
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
#                            ORM
#
#_____________________________________________________________
#|schema/types |sql expresions |              engine          |
#|_____________|_______________|______________________________|
#                              | connection pool | dialect    |
#                              |______________________________|
#
#                                            DBAPI


engine = create_engine('sqlite:///:memory:', echo=True)
session.configure(bind=engine)
Base.metadata.bind = engine
Base.metadata.create_all()



# obj = model.Table()
# session.add(obj)
# session.delete(obj)
# q = session.query(model.tableClass)
# q.all(), q.first(), q.get(1), q[2:5],

# Filter[_by] function: can use and_, or_ and not_ logic operators as parameters
# list of entities = q.filter(model.tableClass.columnname==expr), q.filter_by(columnname=expr),
# another query object = q.filter(model.tablename.c.columname.like), q.filter_by()

# using sqlexpressions using the orm session
# s = select([model.tablename])
# session.execute(s)


