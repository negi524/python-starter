# python-starter
Pythonのプロジェクトテンプレート

## プロジェクトインストール

```bash
poetry install
```

## credentialファイル作成

```bash
cp python_starter/.env.sample python_starter/.env
```

## プログラム実行

```bash
poetry run python python_starter/main.py
```

or 

```bash
make main
```

## フォーマット

```bash
make format
```

## テスト実行

```bash
make test
```

## 型チェック

```bash
make type-check
```

## 全てまとめてチェック

```bash
make format test type-check
```

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
