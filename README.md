# hatena-blog-poster
はてなアカウントのOAuth認証を行いはてなブログへ自動投稿するための簡単なスクリプト。  

## ファイル構成
- `hatenablog_poster.py` - メイン投稿スクリプト
- `token_request.py` - OAuth認証フロー
- `.env.sample` - 環境変数テンプレート

## 必要な環境 / 依存関係
- Python 3.10以上
  - `requests-oauthlib`
  -  `python-dotenv`  

```bash
pip install -r requirements.txt
```

## セットアップ

### 1.  OAuth認証用情報の取得（初回のみ）
**Consumer KeyとConsumer Secretを取得：**
- https://developer.hatena.ne.jp/ja/documents/auth/apis/oauth/consumer を参照
- `.env`に以下を設定：  

```env
HATENA_CONSUMER_KEY=Your_consumer_key
HATENA_CONSUMER_SECRET=Your_consumer_secret
```

**投稿用エンドポイントを作成・設定：**
```env
HATENA_ENTRY_URL=https://blog.hatena.ne.jp/{あなたのはてなID}/{あなたのブログID}/atom/entry
```

### 2. アクセストークンの取得
```bash
python token_request.py
```

- ターミナルに表示されたURLをブラウザで開く
- はてなでOAuth認証を完了
- 表示される認証キーをターミナルに入力
- 取得したトークンを`.env`に追記：
```env
HATENA_ACCESS_TOKEN=your_access_token
HATENA_ACCESS_TOKEN_SECRET=your_access_token_secret
```

## 投稿のテスト

上記手順後hatena_blog_poster.pyを実行。表示されるURLへアクセス。投稿を確認します。

```bash
python token_request.py
```

- スクリプトのデフォルトはマークダウン記法
- ただし、マークダウンの内容を正しく表示させるには、予めはてな側の設定で記法を選択しておくこと必要です。

## 内部フロー

1. `xml_unparser()` - 投稿データをAtom形式のXMLに変換
2. `hatena_oauth()` - OAuth1認証でAPIリクエスト送信
3. `parse_response()` - はてなからのレスポンスを解析
4. 投稿結果を辞書で返却

## ライセンス
MIT License
