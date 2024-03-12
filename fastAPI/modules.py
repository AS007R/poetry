from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class Role(str, Enum):
  user:str = "user"
  admin:str = "admin"
  student:str = "student"


class Gender(str, Enum):
  male:str = "male"
  female:str = "female"


class User(BaseModel):
  id: int
  full_name: str
  gender:Gender
  roles:List[Role]


class updateUserDetails(BaseModel):
  full_name: Optional[str]
  roles:Optional[List[Role]]