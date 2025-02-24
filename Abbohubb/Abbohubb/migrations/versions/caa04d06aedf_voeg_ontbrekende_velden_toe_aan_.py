"""Voeg ontbrekende velden toe aan abonnementen

Revision ID: caa04d06aedf
Revises: d4845d62db61
Create Date: 2025-02-08 09:43:42.857187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caa04d06aedf'
down_revision = 'd4845d62db61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('abonnement', schema=None) as batch_op:
        batch_op.add_column(sa.Column('frequentie_bezorging', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('prijs_vanaf', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('prijs_tot', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('wat_is_het_abonnement', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('waarom_kiezen', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('hoe_werkt_het', sa.Text(), nullable=True))
        batch_op.add_column(sa.Column('past_dit_bij_jou', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('abonnement', schema=None) as batch_op:
        batch_op.drop_column('past_dit_bij_jou')
        batch_op.drop_column('hoe_werkt_het')
        batch_op.drop_column('waarom_kiezen')
        batch_op.drop_column('wat_is_het_abonnement')
        batch_op.drop_column('prijs_tot')
        batch_op.drop_column('prijs_vanaf')
        batch_op.drop_column('frequentie_bezorging')

    # ### end Alembic commands ###
