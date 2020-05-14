from .db_intf.twitter-neo4j.docker.features.fetcher_query import fetcher_query_store

def store_fetch_query(request):
    #TODO : Fetch query and the user info
    queries = fetcher_query_store(queries, user)
    return queries