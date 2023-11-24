from pydantic import BaseModel

from typing import Literal, Dict
from datetime import datetime
import re

EnumField = Literal["email", "phone", "date", "text"]

class FormTamplateModel(BaseModel):
    name: str
    fields: Dict[str, EnumField]


def get_type_value(value:str) -> EnumField:
    if not isinstance(value, str):
        raise ValueError
    for fmt in ("%d.%m.%Y", "%Y-%m-%d"):
        try:
            datetime.strptime(value, fmt)
            return "date"
        except ValueError:
            pass
    if re.fullmatch(r'\+7\D{0,2}\d{3}\D{0,2}\d{3}\D{0,1}\d{2}\D{0,1}\d{2}', value) is not None:
        return "phone"
    if re.fullmatch(r'.+@.+\..+', value) is not None:
        return "email"
    return "text"