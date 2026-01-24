# python-starter
Pythonのプロジェクトテンプレート

## プロジェクトインストール

```bash
uv sync
```

## credentialファイル作成

```bash
cp src/.env.sample src/.env
```

## プログラム実行

```bash
uv run python src/main.py
```

## その他コマンド

[mise.toml](./mise.toml)
## リポジトリのバージョンアップ

```bash
uv version --bump patch
```
