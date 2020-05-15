from .neo4jintf.docker.features.fetcher_query import fetcher_query_store

def store_fetch_query(query, user):
    #TODO : Fetch query and the user info
    
    fields = ['search_term', 'categories', 'need_filter' ]
    query_json = {}
    for key, value in query.items():
        if key in fields:
            query_json[key] = value
    if 'need_filter' in query_json and query_json['need_filter']=='on':
        filter_json = {"retweets_of":query['retweets_of']}
        query_json['tweet_filter'] = filter_json
        query_json['need_filter']='yes'
    else:
        query_json['need_filter']='no'

    queries = [query_json]
    userinfo = {'username':user.username, 'email':user.email}
    status = fetcher_query_store.add_new_query(queries=queries, user=userinfo)
    return status