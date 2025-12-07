# hatenablog-poster
はてなアカウントのOAuth認証を行いはてなブログへ自動投稿するための簡単なスクリプト。  

## ファイル構成
- `hatenablog_poster.py` - メイン投稿スクリプト
- `token_request.py` - OAuth認証フロー
- `.env.sample` - 環境変数テンプレート

## 必要な環境 / 依存関係
- Python 3.10以上
  - `requests-oauthlib`
  - `python-dotenv`  

## 使用方法

- セットアップ完了後、`hatenablog_poster.py`から関数をインポートして使用：

```python
from hatenablog_poster import blog_post

result = blog_post(
    title="記事タイトル",
    content="記事本文",
    categories=["カテゴリ1", "カテゴリ2"],
    is_draft=False,
)

print(result["link_alternate"])  # 投稿URLを表示
print(result["link_edit_user"])  # 編集用URLを表示
```

## セットアップ

### 1. 依存ライブラリのインストール
```bash
pip install -r requirements.txt
```

### 2.  OAuth認証用情報の取得
**Consumer KeyとConsumer Secretを取得：**
- https://developer.hatena.ne.jp/ja/documents/auth/apis/oauth/consumer を参照
- `.env`を作成し以下を設定：  

```env
HATENA_CONSUMER_KEY=Your_consumer_key
HATENA_CONSUMER_SECRET=Your_consumer_secret
```

**投稿用エンドポイントを作成・`.env`で設定：**
```env
HATENA_ENTRY_URL=https://blog.hatena.ne.jp/{あなたのはてなID}/{あなたのブログID}/atom/entry
```

### 3. アクセストークンの取得
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

- 上記手順後`hatenablog_poster.py`を実行。表示されるURLへアクセス。投稿を確認します。

```bash
python hatenablog_poster.py
```

- 本文のデフォルトはマークダウン記法
- ただし、マークダウンの内容を正しく表示させるには、予めはてな側の設定で記法を選択しておくことが必要です。


## 内部フロー

1. `xml_unparser()` - 投稿データをAtom形式のXMLに変換
2. `hatena_oauth()` - OAuth1認証でAPIリクエスト送信
3. `parse_response()` - はてなからのレスポンスを解析
4. 投稿結果を辞書で返却

## ライセンス
MIT License
