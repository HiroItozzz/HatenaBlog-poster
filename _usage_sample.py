from hatenablog_poster import blog_post

result = blog_post(
    title="記事タイトル",
    content="記事本文",
    categories=["カテゴリ1", "カテゴリ2"],
    is_draft=False,
)

print(result["link_alternate"])  # 投稿URLを表示
print(result["link_edit_user"])  # 編集用URLを表示
