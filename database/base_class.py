from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    """ Base class that overloads the table name """
    __name__: str

    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
