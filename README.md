# python-starter
Pythonのプロジェクトテンプレート

## プロジェクトインストール

```bash
poetry install
```

## credentialファイル作成

```bash
cp python_starter/config/credential-sample.yml python_starter/config/credential.yml
```

## プログラム実行

```bash
poetry run python python_starter/main.py
```

or 

```bash
poetry run dev
```

## フォーマット

```bash
poetry run black python_starter/ tests/
```

## テスト実行

```bash
poetry run pytest tests/