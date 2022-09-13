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
  
  return g.db

#g.dbが設定されているかを調べ、設定されている場合はconnectionを閉じる関数。各リクエストの後にclose_db()を呼び出すことになるようだ。
def close_db(e=None):
  db = g.pop('db', None) #gからdb要素を持ってくる。存在しない場合はNoneを返す。

  if db is not None: #dbが存在している場合は
    db.close()       #connectionを閉じる