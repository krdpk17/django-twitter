from .neo4jintf.docker.features.fetcher_query import fetcher_query_store

def fetch_all_queries_by_user(user):
    userinfo = {'username':user.username, 'email':user.email}
    queries = fetcher_query_store.fetch_all_queries_by_user(user=userinfo)
    return queries

def apply_list_type(data_dict, list_type_fields):
    for key, value in data_dict.items():
        if key in list_type_fields:
            value_split = value.split()
            data_dict[key] = value_split

def store_fetch_query(query, user):
    #Fetch query and the user info
    fields = ['search_term', 'categories']
    list_type_fields = ['categories', 'retweets_of']
    query_json = {}
    for key, value in query.items():
        if key in fields:
            query_json[key] = value
    
    if 'need_filter' in query and query['need_filter']=='on':
        filter_json = {"retweets_of":query['retweets_of']}
        apply_list_type(filter_json, list_type_fields)
        query_json['tweet_filter'] = filter_json
        query_json['filter']='on'
    else:
        query_json['filter']='off'
    apply_list_type(query_json, list_type_fields)
    search_query_json = {"tweet_search":query_json}
    queries = [search_query_json]
    userinfo = {'username':user.username, 'email':user.email}
    status = fetcher_query_store.add_new_query(queries=queries, user=userinfo)
    return status