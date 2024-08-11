"""Update password_hash column size

Revision ID: ac041a536955
Revises: b77400a75b67
Create Date: 2024-08-11 11:22:54.796428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac041a536955'
down_revision = 'b77400a75b67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
        batch_op.alter_column('username',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)

    # ### end Alembic commands ###
