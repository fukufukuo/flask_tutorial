import flask

app = flask.Flask(__name__) #Flaskクラスのインスタンス生成、appに格納

@app.route('/') #appにおいて、/というURLに対応するアクションを以下に記述する
def index():
  return 'Hello, Flask!'

if __name__ == '__main__': #ファイルをスクリプトとして直接実行する場合、__name__は__main__となる
  app.run(debug=True) #Flaskが持っている開発サーバーを、デバッグモードで実行