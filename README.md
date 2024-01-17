# これは何？
NovelAIのAPIを叩いて画像を生成するためのツール

# どうやって使うの？
すべてDockerで実行するようにしました \
環境構築の手間を減らしました

## DockerDesktopをインストール 
* [Install Docker Desktop on Mac \| Docker Docs](https://docs.docker.com/desktop/install/mac-install/)
* [Install Docker Desktop on Windows \| Docker Docs](https://docs.docker.com/desktop/install/windows-install/)

## .envを用意
* .env.exampleを用意しているのでそちらをコピーして記入してください。

|key|内容|参考|
|---|---|---|
|NAI_USERNAME|NovelAIで利用しているユーザー名を記入|mailaddress@example.com|
|NAI_PASSWORD| NovelAIで利用しているパスワードを記入|外部に流出させてはいけません|
|STORAGE_PATH|/storage|変更しないほうがおすすめ|


## docker_start.shを実行して起動させる
* docker_start.shを実行 \
大体1分ぐらいで起動する
```
$ /bin/sh docker_start.sh
```
* アクセスする
```
open "http://localhost:8051"
```
