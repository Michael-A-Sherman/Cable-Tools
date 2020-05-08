import requests

# Uses Pathtrak API to search for node
# Returns search results as list in JSON format
def pathtrak_search(baselink, user_query):
    url = baselink + 'api/elements/search/' + user_query
    get_data = requests.get(url, "accept: application/json", verify=False)
    return get_data.json()

def spectrum_view(base_link, node):
    if len(node) == 1:
        return base_link + 'spectrum/view.html#/hcu/' + str(node[0]["id"])  # pulls id element from results
    else:
        results = []
        for nodes in node:
            results.append(nodes)
        return results