"""Voeg nieuwe velden toe aan abonnementen

Revision ID: d4845d62db61
Revises: 3c9f10954c78
Create Date: 2025-02-08 09:20:16.624687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4845d62db61'
down_revision = '3c9f10954c78'
branch_labels = None
depends_on = None


def upgrade():
    # Voeg de nieuwe kolommen toe aan de abonnementen-tabel
    op.add_column('abonnement', sa.Column('frequentie_bezorging', sa.String(50), nullable=True))
    op.add_column('abonnement', sa.Column('prijs_vanaf', sa.Float, nullable=True))
    op.add_column('abonnement', sa.Column('prijs_tot', sa.Float, nullable=True))
    op.add_column('abonnement', sa.Column('wat_is_het_abonnement', sa.Text, nullable=True))
    op.add_column('abonnement', sa.Column('waarom_kiezen', sa.Text, nullable=True))
    op.add_column('abonnement', sa.Column('hoe_werkt_het', sa.Text, nullable=True))
    op.add_column('abonnement', sa.Column('past_dit_bij_jou', sa.Text, nullable=True))


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chatbot_logs',
    sa.Column('vraag', sa.TEXT(), nullable=True),
    sa.Column('antwoord', sa.TEXT(), nullable=True)
    )
    op.create_table('chatbot_log',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('vraag', sa.VARCHAR(length=255), nullable=False),
    sa.Column('antwoord', sa.VARCHAR(length=255), nullable=False),
    sa.Column('timestamp', sa.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
