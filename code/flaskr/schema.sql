-- 空の表の作成
-- ユーザ情報をuser表に、投稿記事はpost表に格納

DROP TABLE IF EXISTS user; --user表が存在していたら、user表を削除
DROP TABLE IF EXISTS post;

CREATE TABLE user(
  id INTEGER PRIMARY KEY AUTOINCREMENT, --idは主キーで自動採番
  username TEXT UNIQUE NOT NULL, -- usernameは重複禁止
  password TEXT NOT NULL
);

CREATE TABLE post(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, --2022-09-18 11:35:23:047 の形式のタイムスタンプ
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id) --author idを外部キーとする。参照する親キーは、userテーブルのid列。
);
