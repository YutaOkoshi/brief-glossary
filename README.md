# 各ファイル説明

```
brief-glossary
├── README.md
├── brief-glossary  # アプリディレクトリ
│   ├── config      #各種設定
|   〜中略〜
│   └── manage.py
├── docker
│   ├── db
│   │   └── Dockerfile
│   └── web
│       └── Dockerfile
├── docker-compose.yml
├── example.bashrc
├── requirements.txt
└── wait-for-it.sh
```

# 開発者向けの手順 - コンテナーとVS Codeで開発する場合

## 前提
```
$ docker -v
Docker version 19.03.8, build afacb8b
$ docker-compose -v
docker-compose version 1.25.5, build 8a1c60f6
```

##  手順
```
$ docker-compose build

$ docker-compose up
# ※初回起動時はdbの起動タイミングによっては失敗するので何度か実行してください。
# TODO: 後々wait-for-it.sh使って実装する

$ docker ps
# brief-glossary_webコンテナのSTATUSが up ならOK

# あとはVS Codeからコンテナーに繋ぎ開発！
# 詳細は「https://qiita.com/Yuki_Oshima/items/d3b52c553387685460b0」
```

# URL

- 管理画面
    - http://localhost:8000/admin/login/?next=/admin/


#  開発時に覚えておくと役立つコマンド

以下手順はすべてコンテナー内で実行しています。

## マイグレーションファイル作成
```
$ python manage.py makemigrations
```

## マイグレーション実行
```
$ python manage.py migrate
```

## 管理者ユーザー作成コマンド
```
$ python manage.py createsuperuser
```

## マイグレーションファイルのスカッシュ
```
$ python manage.py squashmigrations brief-glossary 0050_remove_book_price
```

## Docker環境の断捨離
```
$ docker system prune  -a
```

