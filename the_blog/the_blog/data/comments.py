import datetime
import sqlalchemy
from uuid import uuid4

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from the_blog.data.sqlbasetype import SqlAlchemyBase


class Comment(SqlAlchemyBase):
    __tablename__ = "comments"
    id = sqlalchemy.Column(
        sqlalchemy.Text,
        primary_key=True,
        default=lambda: str(uuid4()).replace('-', '')[:8])

    created = sqlalchemy.Column(
        sqlalchemy.DateTime,
        default=datetime.datetime.now,
        index=True)
    text = sqlalchemy.Column(sqlalchemy.Text)
    post_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('posts.id'))
    post = relationship("Post", back_populates="comments")
