#SQLiteのインポート
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

#データベースを取得する関数
def get_db():
  if 'db' not in g:
    #current_app.configの、キーDATABASEで示されるファイルへのconnectionを確立
    g.db = sqlite3.connect(
      current_app.config['DATABASE'],
      detect_types=sqlite3.PARSE_DECLTYPES
    ) # このファイルは、init_db()で初期化するまでは存在していない
    g.db.row_factory = sqlite3.Row
  
  return g.db

#g.dbが設定されているかを調べ、設定されている場合はconnectionを閉じる関数。各リクエストの後にclose_db()を呼び出すことになるようだ。
def close_db(e=None):
  db = g.pop('db', None) #gからdb要素を持ってくる。存在しない場合はNoneを返す。

  if db is not None: #dbが存在している場合は
    db.close()       #connectionを閉じる

#schema.sqlに書いたsqlコマンドを実行するinit_db()関数の定義
def init_db():
  db = get_db() #dbの取得

  with current_app.open_resource('schema.sql') as f: #アプリケーションからの相対パスで指定したSQLファイルを開く。同じ階層にSQLファイルがあるのでこのように書ける
    db.executescript(f.read().decode('utf8')) #読み込んだものはバイト列になるので、utf8でデコード(文字列化)する

@click.command('init-db') #このデコレータはこのスクリプトの中には書いていないので、clickで標準で準備されている関数のはず。
@with_appcontext #アプリ実行のコンテクスト(環境)で使われることを保証する(?)
#理解のためには、元関数も必要だと思うので、内容を理解はしていないが写経する。
def init_db_command():
  """Clear the existing data and create new tables.""" #突然文字列書いていいんですか？・・ドキュメントストリング参照
  init_db()
  click.echo('Initialized the database.')

#flaskrアプリケーションに、close_db()と、init_db_command()を登録する
def init_app(app):
  app.teardown_appcontext(close_db) #アプリケーションのcontextが終了するときに呼び出す関数を登録する
  app.cli.add_command(init_db_command)
#→factoryでこの関数をimportする。__init__.py参照