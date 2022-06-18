import pydantic


class ORMBaseModel(pydantic.BaseModel):
    class Config:
        orm_mode = True
