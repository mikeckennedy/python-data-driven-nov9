import datetime
import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from the_blog.data.sqlbasetype import SqlAlchemyBase
from the_blog.data.comments import Comment

class Post(SqlAlchemyBase):
    __tablename__ = "posts"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    pub_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    content = sqlalchemy.Column(sqlalchemy.Text, nullable=True)
    url = sqlalchemy.Column(sqlalchemy.Text, index=True, nullable=False, unique=True)
    comments = sqlalchemy.orm.relationship("Comment", back_populates="post")

#
# class Post:
#     title = None
#     pub_date = datetime.datetime.now()
#     content = None
#     url = None
#
#     def __init__(self, title, content, url):
#         self.url = url
#         self.content = content
#         self.title = title
