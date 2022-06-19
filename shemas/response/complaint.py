from datetime import datetime

from models import State
from shemas.base import BaseComplaint


class ComplaintOut(BaseComplaint):
    id: int
    created_at: datetime
    status: State
