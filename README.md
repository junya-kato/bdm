# BDM class repo

### セットアップ

python3 系でしか動きません

#### ラズパイにモータをつけて動かすとき

```
# shellで
$ python main.py
# or
$ python3 main.py
```

#### モータをつながずに動かす場合

標準出力にモータの回転角が表示されます

```
# shellで
$ GAME_ENV=dev python main.py
# or
$ GAME_ENV=dev python3 main.py
```

### git 使い方

#### 編集したファイルをアップロードするとき

1. アップロードするファイルを決める staging

```
# 全部のとき
git add -A
# 一部のとき
git add <file名>
```

2. コミット 変更を確定する。(ローカルで)

```
git commit
# 変更した内容(commit log) を示す
git commit -m "<commit log>"
```

3. プッシュ リモートリポジトリにコミット内容をコピー

```
git push
# or
git push origin master
```

#### 編集された内容を取ってくる

```
git pull
```

#### 変更しているファイルがあるかどうか見たいとき(staging されているか sareteiruka)

```
git status
```

#### commit したかどうか(origin/master は リモート HEAD -> master はローカル)

```
git log
```

Q で終了
