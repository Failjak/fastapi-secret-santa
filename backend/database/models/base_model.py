from pydantic import BaseModel


class ORMBaseModel(BaseModel):
    """
    Base class with the orm_mode parameter set to True
    """
    class Config:
        orm_mode = True
