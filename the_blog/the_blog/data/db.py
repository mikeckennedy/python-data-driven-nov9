# noinspection PyUnresolvedReferences
import the_blog.data.posts
# noinspection PyUnresolvedReferences
import the_blog.data.comments
from the_blog.data.sqlbasetype import SqlAlchemyBase

import sqlalchemy
import sqlalchemy.orm
import os


# print("__file__ = " + __file__)

web_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# print("web root: " + web_root)

db_file = os.path.join(web_root, 'data_store', 'blog.sqlite')
# print(db_file)

conn_string = 'sqlite:///' + db_file

# one engine per connection string
engine = sqlalchemy.create_engine(conn_string, echo=True)  # , echo=True)
# one base class per DB
SqlAlchemyBase.metadata.create_all(engine)
# one factory per db
session_factory = sqlalchemy.orm.sessionmaker(engine)
