import sqlite3,click, json
from flask import current_app, g, json
from static import utils
DATABASE = "./databases/ortbialBodies.db"

def get_db():
    # What is g? RESEARCH NEEDED
    if 'db' not in g:
        # Create/open the DATABASE
        # Not sure what PARSE_DECLTYPES does. RESEARCH NEEDED
        g.db = sqlite3.connect(DATABASE, detect_types=sqlite3.PARSE_DECLTYPES)
        # not sure what row_factory does. RESEARCH NEEDED
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():

    # connect to the database file, if created then open
    db = get_db()

    # execute the  sql code as written in schema.sql
    # Research needed into how the stream is operating here!
    with current_app.open_resource('databases/schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def insert_Data(data):
    db = get_db()
    decoded_json = utils.json_decode(data)  
    # Delete orbitalBodiesDB.old
    db.execute("""DELETE FROM orbitalBodies;""")
    
    count = 1
    for characteristic in decoded_json:
        utils.orbitalBodiesSQLInsert(characteristic, count, db)
        count += 1

    # commit changes to database and close 
    db.commit()
    close_db()
    
    return None


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
