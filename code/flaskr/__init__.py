import os
#osモジュールを使えるようにする

from flask import Flask
#flaskパッケージから、Flaskクラスをインポート

def create_app(test_config=None):
#create_app()という変数の定義開始 引数test_configのデフォルト値がNone
  app = Flask(__name__, instance_relative_config=True)
  #appにFlaskインスタンスを代入
  app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), #インスタンスフォルダ直下に、SQLiteデータベースを配置
    )