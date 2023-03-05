import yaml
from pathlib import Path
from typing import Optional

credential_file_path: str = (
    f"{Path(__file__).resolve().parent.parent}/config/credential.yml"
)


def read_credential() -> Optional[dict]:
    """credential情報を読み込み、辞書型で返却する
    Returns:
        dict: credential.ymlに記載された情報
    """
    with open(credential_file_path) as file:
        return yaml.safe_load(file)
