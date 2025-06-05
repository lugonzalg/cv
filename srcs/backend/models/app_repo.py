from pydantic import BaseModel

# This class is the database model, we need to
# initialize the model with a method

# Before this we need a dbclient in ../data/pgdatabase.py
# Will have an initialize method to start the connection
# and start the models

class AppRepos(BaseModel):
    name: str
    description: str
    skills: list[str]
    repo_url: str
