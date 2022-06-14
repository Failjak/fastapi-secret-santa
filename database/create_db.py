from database import Base
from database.session import engine

print("Creating database . . .")

Base.metadata.create_all(engine)
