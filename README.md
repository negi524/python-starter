# python-starter
Pythonのプロジェクトテンプレート

## プロジェクトインストール

```bash
poetry install
```

## credentialファイル作成

```bash
cp src/.env.sample src/.env
```

## プログラム実行

```bash
poetry run python src/main.py
```

## その他コマンド

[mise.toml](./mise.toml)
## リポジトリのバージョンアップ

```bash
poetry version <バージョン>
```

## パッケージのバージョンアップ

```bash
poetry search <パッケージ名>
```

`pyproject.toml`を確認し、必要であれば制約を修正する。
その後

```bash
poetry update
```

[poetry documentation](https://python-poetry.org/docs/cli/#update)
