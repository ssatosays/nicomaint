# nicomaint
ニコニコ動画のメンテナンス・障害・復旧を[公式サイト](https://blog.nicovideo.jp/niconews/category/ge_maintenance/)から取得

## 実行結果
```
ssatosays@local(19:59:00)(2) ~ $ curl http://127.0.0.1:5000/ |jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  5964  100  5964    0     0   5701      0  0:00:01  0:00:01 --:--:--  5701
[
  {
    "date": "2022-02-01",
    "index": 1,
    "title": "【2/1追記・調査中】GoogleChromeブラウザで、まれに動画再生が停止する不具合【PC版ニコニコ動画】",
    "url": "https://blog.nicovideo.jp/niconews/164044.html"
  },
  {
    "date": "2022-01-28",
    "index": 2,
    "title": "クリエイター奨励プログラム 予想スコアの反映遅延について",
    "url": "https://blog.nicovideo.jp/niconews/164815.html"
  },
...
  {
    "date": "2021-12-10",
    "index": 17,
    "title": "他社流出パスワードを用いた不正ログインについて(2021/12)",
    "url": "https://blog.nicovideo.jp/niconews/162387.html"
  }
]
```

## ニコニコ規約
> 5 禁止事項  
> ｢ニコニコ｣のサーバーに過度の負担を及ぼす行為

[ニコニコ規約](https://account.nicovideo.jp/rules/account)より
