from models import RoleType
from shemas.base import UserBase


class UserOut(UserBase):
    id: int
    phone: str
    first_name: str
    last_name: str
    iban: str
    role: RoleType
