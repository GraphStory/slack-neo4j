import requests
import os
import re
import time
from py2neo import Graph

url = os.environ.get('NEO4J_URL',"http://localhost:7474/db/data/")
graph = Graph(url)


def init():
    # Add uniqueness constraints.
    graph.cypher.execute("CREATE CONSTRAINT ON (c:Channel) ASSERT t.id IS UNIQUE;")
    graph.cypher.execute("CREATE CONSTRAINT ON (u:User) ASSERT u.id IS UNIQUE;")
    graph.cypher.execute("CREATE INDEX ON :User(name);")
    graph.cypher.execute("CREATE INDEX ON :Channel(name);")
        

def overview():
    query = """
    MATCH (c:Channel)
    OPTIONAL MATCH (c)-[r]-() 
    RETURN c.name, type(r), count(*) as cnt
    ORDER BY cnt DESC LIMIT 5
    """
    rows = graph.cypher.execute(query)
    return rows

def isUpdate(query):
    return re.match("(create|merge|delete|set|remove|drop)",query,flags=re.IGNORECASE)
    
def cypher(query):
    if isUpdate(query):
        return "Only read-only queries allowed"        
    rows = graph.cypher.execute(query)
    return rows


if __name__ == "__main__":
    print overview()
