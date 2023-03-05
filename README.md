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