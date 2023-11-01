"""empty message

Revision ID: 389a79c91fed
Revises:
Create Date: 2023-10-31 22:32:35.746503

"""
from alembic import op
import sqlalchemy as sa
import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")


# revision identifiers, used by Alembic.
revision = '389a79c91fed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )

    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")

    # op.create_table('products',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('owner_id', sa.Integer(), nullable=True),
    # sa.Column('title', sa.String(length=50), nullable=False),
    # sa.Column('photo_url', sa.String(), nullable=False),
    # sa.Column('description', sa.String(length=1000), nullable=False),
    # sa.Column('size', sa.String(length=15), nullable=False),
    # sa.Column('price', sa.Integer(), nullable=False),
    # sa.Column('created_at', sa.Date(), nullable=False),
    # sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )

    # if environment == "production":
    #     op.execute(f"ALTER TABLE products SET SCHEMA {SCHEMA};")


    # op.create_table('reviews',
    # sa.Column('id', sa.Integer(), nullable=False),
    # sa.Column('user_id', sa.Integer(), nullable=False),
    # sa.Column('product_id', sa.Integer(), nullable=False),
    # sa.Column('review', sa.String(length=1000), nullable=False),
    # sa.Column('created_at', sa.Date(), nullable=False),
    # sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    # sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    # sa.PrimaryKeyConstraint('id')
    # )

    # if environment == "production":
    #     op.execute(f"ALTER TABLE reviews SET SCHEMA {SCHEMA};")


    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('reviews')
    # op.drop_table('products')
    op.drop_table('users')
    # ### end Alembic commands ###
