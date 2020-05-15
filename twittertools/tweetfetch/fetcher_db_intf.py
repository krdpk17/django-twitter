from .neo4jintf.docker.features.fetcher_query import fetcher_query_store

def store_fetch_query(query, user):
    #TODO : Fetch query and the user info
    queries = [query]
    status = fetcher_query_store(queries, user)
    return status