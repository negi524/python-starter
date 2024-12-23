from pydantic import BaseModel


class User(BaseModel):
    """Userクラス"""

    id: int
    name: str
