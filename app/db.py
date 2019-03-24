# -*- coding: utf-8 -*-

import sqlite3
import click
import xlrd

from flask import current_app, g
from flask.cli import with_appcontext


def set_data(name, type, address):
    print(name, type, address)
    db = get_db()
    db.execute(
        'INSERT INTO restaurant (name, type, address)'
        ' VALUES (?, ?, ?)',
        (name, type, address)
    )
    db.commit()


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    try:
        wb = xlrd.open_workbook(current_app.config['DATA_PATH'])
    except IOError:
        wb = xlrd.open_workbook('guide/db.xlsx')
    sheet = wb.sheet_by_index(0)

    row = 1
    while row < sheet.nrows:
        row_value = sheet.row_values(row)
        # set_data('식당이름', '식당종류', '주소')
        set_data(row_value[1], row_value[2], row_value[3])
        row += 1


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
