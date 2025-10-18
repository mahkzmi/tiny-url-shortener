import shortuuid
import re

CODE_REGEX = re.compile(r'^[A-Za-z0-9\-_]{3,32}$')

def generate_code(length: int = 6) -> str:
    return shortuuid.ShortUUID().random(length=length)

def validate_custom_code(code: str) -> bool:
    return bool(CODE_REGEX.match(code))
