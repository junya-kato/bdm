# BDM class repo

## git 使い方

### 編集したファイルをアップロードするとき
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

##  編集された内容を取ってくる

```
git pull
```

##  変更しているファイルがあるかどうか見たいとき(stagingされているかsareteiruka)
```
git status
```

## commitしたかどうか(origin/master は リモート HEAD -> master はローカル)
```
git log
```
Qで終了