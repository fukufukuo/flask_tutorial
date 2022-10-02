import os
#osモジュールを使えるようにする

from flask import Flask
#flaskパッケージから、Flaskクラスをインポート

def create_app(test_config=None): #これがいわゆるfactory
#create_app()という変数の定義開始 引数test_configのデフォルト値がNone
  app = Flask(__name__, instance_relative_config=True)
  #appにFlaskインスタンスを代入
  app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), #インスタンスフォルダ直下に、SQLiteデータベースを配置
    )
  
  if test_config is None:
    # instance configを読み込む テスト環境じゃないとき
    app.config.from_pyfile('config.py', silent=True)
  else:
    # テストコンフィグを読み込む
    app.config.from_mapping(test_config)
  
  #インスタンスフォルダの存在チェック
  try:
    os.makedirs(app.instance_path) #インスタンスパスのフォルダを作成
  except OSError:
    pass #すでにインスタンスパスのフォルダが存在するときはエラーを吐く。その場合は何も実行しない

  # a simple page that says hello
  @app.route('/hello')
  def hello():
    return 'Hello, World!'
  
  #db.pyで定義した関数を実行→アプリケーションに、db.pyで定義した関数が登録される
  from . import db
  db.init_app(app)

  from . import auth #このファイルと同じ階層にあるauth.pyをインポート
  app.register_blueprint(auth.bp) #auth.py内のbpをblueprintとして登録

  return app

    