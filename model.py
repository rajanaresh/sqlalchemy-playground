import datetime
from sqlalchemy import schema, types
from sqlalchemy import orm
from sqlalchemy.ext.declarative import declarative_base


# schema.Table
# schema.Column
# schema.MetaData()


sm = orm.sessionmaker(autoflush=True, autocommit=False, expire_on_commit=True)
session = orm.scoped_session(sm)
Base = declarative_base()

def now():
    return datetime.datetime.now()

pagetag_table = schema.Table('pagetag', Base.metadata,
    schema.Column('id', types.Integer,
        schema.Sequence('pagetag_seq_id', optional=True), primary_key=True),
    schema.Column('pageid', types.Integer, schema.ForeignKey('pages.id')),
    schema.Column('tagid', types.Integer, schema.ForeignKey('tags.id')),
)

class Page(Base):
    __tablename__ = 'pages'
    id = schema.Column(types.Integer, schema.Sequence('page_seq_id', optional=True), primary_key=True)
    content = schema.Column(types.Text(), nullable=False)
    posted = schema.Column(types.DateTime(), default=now)
    title = schema.Column(types.Unicode(255), default=u'Untitled Page')
    heading = schema.Column(types.Unicode(255))
    gender = schema.Column(types.Enum('male', 'female'))

    comments = orm.relationship("Comment", backref='page')

    tags = orm.relationship('Tag', secondary=pagetag_table, backref='pages')

class Comment(Base):
    __tablename__ = 'comments'
    id = schema.Column(types.Integer, schema.Sequence('comment_seq_id', optional=True), primary_key=True)
    pageid = schema.Column(types.Integer, schema.ForeignKey('pages.id'), nullable=False)
    content = schema.Column(types.Text(), default=u'')
    name = schema.Column(types.Unicode(255))
    email = schema.Column(types.Unicode(255), nullable=False)
    created = schema.Column(types.TIMESTAMP(), default=now)   

class Tag(Base):
    __tablename__ = 'tags'
    id = schema.Column(types.Integer, schema.Sequence('tag_seq_id', optional=True), primary_key=True)
    name = schema.Column(types.Unicode(20), nullable=False, unique=True)

