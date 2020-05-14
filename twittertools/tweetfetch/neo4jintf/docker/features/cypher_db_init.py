
'''
Built-in modules
'''
import pdb
import os


from config.load_config import load_config
config_file_name = 'env.py'
load_config(config_file_name)

from libs.cypher_store import DMCypherDBInit

constraint_list = [
    "CREATE CONSTRAINT ON (t:Tweet) ASSERT t.id IS UNIQUE;",
    "CREATE CONSTRAINT ON (u:User) ASSERT u.screen_name IS UNIQUE;",
    "CREATE CONSTRAINT ON (u:User) ASSERT u.id IS UNIQUE;",
    "CREATE CONSTRAINT ON (h:Hashtag) ASSERT h.name IS UNIQUE;",
    "CREATE CONSTRAINT ON (l:Link) ASSERT l.url IS UNIQUE;",
    "CREATE CONSTRAINT ON (s:Source) ASSERT s.name IS UNIQUE;",
    "CREATE CONSTRAINT ON (c:Category) ASSERT c.name IS UNIQUE;"

]

if __name__ == "__main__":
	DMCypherDBInit.create_constraints(constraint_list)