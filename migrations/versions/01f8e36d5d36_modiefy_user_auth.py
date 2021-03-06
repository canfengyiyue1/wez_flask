"""modiefy user_auth

Revision ID: 01f8e36d5d36
Revises: 3377f3e6ef65
Create Date: 2017-08-04 17:51:52.921082

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '01f8e36d5d36'
down_revision = '3377f3e6ef65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'we_zchina_article_cates', 'we_zchina_users', ['zchina_user_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_articles', 'we_zchina_article_cates', ['cate_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_articles', 'we_zchina_users', ['zchina_user_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_module_functions', 'we_zchina_modules', ['module_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_product_function_services', 'we_zchina_users', ['zchina_user_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_product_function_services', 'we_zchina_products', ['product_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_product_function_services', 'we_zchina_product_functions', ['function_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_product_function_services', 'we_zchina_module_functions', ['module_function_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_product_functions', 'we_zchina_products', ['product_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_product_functions', 'we_zchina_module_functions', ['module_function_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_solution_services', 'we_zchina_users', ['zchina_user_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_solution_services', 'we_zchina_solutions', ['solution_id'], ['id'])
    op.add_column('we_zchina_user_auths', sa.Column('address', sa.String(length=100), nullable=True))
    op.add_column('we_zchina_user_auths', sa.Column('birthday', sa.String(length=20), nullable=True))
    op.add_column('we_zchina_user_auths', sa.Column('created_at', sa.Integer(), nullable=True))
    op.add_column('we_zchina_user_auths', sa.Column('id_number', sa.String(length=20), nullable=True))
    op.add_column('we_zchina_user_auths', sa.Column('sex', sa.String(length=10), nullable=True))
    op.add_column('we_zchina_user_auths', sa.Column('updated_at', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'we_zchina_user_auths', 'we_zchina_users', ['zchina_user_id'], ['id'])
    op.drop_column('we_zchina_user_auths', 'id_num')
    op.create_foreign_key(None, 'we_zchina_user_certs', 'we_zchina_users', ['zchina_user_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_user_logs', 'we_zchina_users', ['zchina_user_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_user_types', 'we_zchina_users', ['zchina_user_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_users', 'we_users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'we_zchina_users', 'we_zchinas', ['wezchina_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'we_zchina_users', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_users', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_user_types', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_user_logs', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_user_certs', type_='foreignkey')
    op.add_column('we_zchina_user_auths', sa.Column('id_num', mysql.VARCHAR(length=20), nullable=True))
    op.drop_constraint(None, 'we_zchina_user_auths', type_='foreignkey')
    op.drop_column('we_zchina_user_auths', 'updated_at')
    op.drop_column('we_zchina_user_auths', 'sex')
    op.drop_column('we_zchina_user_auths', 'id_number')
    op.drop_column('we_zchina_user_auths', 'created_at')
    op.drop_column('we_zchina_user_auths', 'birthday')
    op.drop_column('we_zchina_user_auths', 'address')
    op.drop_constraint(None, 'we_zchina_solution_services', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_solution_services', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_product_functions', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_product_functions', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_product_function_services', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_product_function_services', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_product_function_services', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_product_function_services', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_module_functions', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_articles', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_articles', type_='foreignkey')
    op.drop_constraint(None, 'we_zchina_article_cates', type_='foreignkey')
    # ### end Alembic commands ###
