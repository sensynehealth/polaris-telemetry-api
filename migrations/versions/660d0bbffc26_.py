"""empty message

Revision ID: 660d0bbffc26
Revises: 
Create Date: 2018-07-17 15:25:17.877051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '660d0bbffc26'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('desktop',
    sa.Column('uuid', sa.String(length=36), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('created_by_', sa.String(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('modified_by_', sa.String(), nullable=False),
    sa.Column('clinician_id', sa.String(length=36), nullable=False),
    sa.Column('unique_device_code', sa.String(), nullable=False),
    sa.Column('date_first_used_', sa.DateTime(), nullable=False),
    sa.Column('date_first_used_time_zone_', sa.Integer(), nullable=False),
    sa.Column('app_product', sa.String(), nullable=False),
    sa.Column('app_version', sa.String(), nullable=False),
    sa.Column('desktop_os', sa.String(), nullable=False),
    sa.Column('desktop_os_version', sa.String(), nullable=False),
    sa.Column('ip_address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('mobile',
    sa.Column('uuid', sa.String(length=36), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('created_by_', sa.String(), nullable=False),
    sa.Column('modified', sa.DateTime(), nullable=False),
    sa.Column('modified_by_', sa.String(), nullable=False),
    sa.Column('patient_id', sa.String(length=36), nullable=False),
    sa.Column('unique_device_code', sa.String(), nullable=False),
    sa.Column('date_first_launched_', sa.DateTime(), nullable=False),
    sa.Column('date_first_launched_time_zone_', sa.Integer(), nullable=False),
    sa.Column('app_product', sa.String(), nullable=False),
    sa.Column('app_version', sa.String(), nullable=False),
    sa.Column('phone_os', sa.String(), nullable=False),
    sa.Column('phone_os_version', sa.String(), nullable=False),
    sa.Column('manufacturer', sa.String(), nullable=False),
    sa.Column('model', sa.String(), nullable=False),
    sa.Column('display_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mobile')
    op.drop_table('desktop')
    # ### end Alembic commands ###
