"""got rid of unique name on and unique path

Revision ID: 965df4506da5
Revises: 411025f3cdb8
Create Date: 2024-03-29 16:23:46.598357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '965df4506da5'
down_revision = '411025f3cdb8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cats', schema=None) as batch_op:
        batch_op.drop_constraint('cats_name_key', type_='unique')
        batch_op.drop_constraint('cats_path_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('cats', schema=None) as batch_op:
        batch_op.create_unique_constraint('cats_path_key', ['path'])
        batch_op.create_unique_constraint('cats_name_key', ['name'])

    # ### end Alembic commands ###