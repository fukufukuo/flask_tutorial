#ここで作成するblueprintは、新しいユーザの登録と、ログイン/ログアウトのviewを持つようにする

#いんぽーと
from crypt import methods
import functools
from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from flaskr.db import get_db #flaskrディレクトリ内のdb.pyから関数をインポートするときはこんな書き方をするんだね！

#blueprint変数の設定
bp = Blueprint('auth', __name__, url_prefix='./auth') #__name__には、このファイルをモジュールとして読み込む場合はモジュール名、スクリプトとして実行する場合は__main__が入るのだった。
#url_prefixは、blueprintのURLの最初につけるパスのこと。

#ルーティング開始
@bp.route('/register', methods=('GET', 'POST')) #GET, POSTメソッドの使用を許可。URLの/registerとregister()関数のビューを関連付ける。
def register():
  if request.method == 'POST': #ユーザーがformをsubmitした場合
    username = request.form['username'] #request.formはdict型
    password = request.form['password']
    db = get_db()
    error = None

    if not username: #usernameがNoneの場合
      error = 'Username is required.'
    elif not password:
      error = 'Password is required.'
    elif db.execute( #username も passwordも空じゃない場合
      'SELECT id FROM user WHERE username = ?', (username,) #db.executeは?を持つSQLのqueryと、プレースホルダ(?)を置き換える値のタプルを受け取る
      ).fetchone() is not None:
      error = f"User {username} is already registered."
