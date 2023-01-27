# from datetime import datetime
# from sqlalchemy import Column, Integer, TIMESTAMP, UniqueConstraint, ForeignKeyConstraint, Index
# from models.base import Base




# class LikedPost(Base):
#     __tablename__ = "liked_posts"

#     __table_args__ = (UniqueConstraint("user_id", "post_id", name="user_post_unique"),
#                      ForeignKeyConstraint(["user_id"], ["user_id"]))

#     id = Column(Integer, primary_key=True)
#     created_at = Column(TIMESTAMP, default=datetime.utcnow)
#     user_id = Column(Integer)
#     post_id = Column(Integer)


# Index("liked_post_user_id_idx", LikedPost.user_id)



