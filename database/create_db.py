from ..database import Base
from session import engine

print("Creating database . . .")

Base.metadata.create_all(engine)
