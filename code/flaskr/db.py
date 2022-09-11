#SQLiteのインポート
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
  if 'db' not in g:
    #current_app.configの、キーDATABASEで示されるファイルへのconnectionを確立
    g.db = sqlite3.connect(
      current_app.config['DATABASE'],
      detect_types=sqlite3.PARSE_DECLTYPES
    )
    g.db.row_factory = sqlite3.Row