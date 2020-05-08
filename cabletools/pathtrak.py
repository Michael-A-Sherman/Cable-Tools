import requests


# Link for PathTrak server except for the "id" number of the node
base_link = "https://nept01.chartercom.com/pathtrak/spectrum/view.html#/hcu/"
search_link = "https://nept01.chartercom.com/pathtrak/api/elements/search/"

canton_base_link = "http://ptkpapp18.corp.twcable.com/pathtrak/spectrum/view.html#/hcu/"
canton_search_link = "http://ptkpapp18.corp.twcable.com/pathtrak/api/elements/search/"

# Uses Pathtrak API to search for node
# Returns search results as list in JSON format
def search_pathtrak_api(user_input):
    url = search_link + user_input
    get_data = requests.get(url, "accept: application/json", verify=False)
    return get_data.json()


def search(node):
    if len(node) == 1:
        return base_link + str(node[0]["id"])  # pulls id element from results
    else:
        results = []
        for nodes in node:
            results.append(nodes)
        return results


def canton_search(node):
    if len(node) == 1:
        return canton_base_link + str(node[0]["id"])  # pulls id element from results
    else:
        results = []
        for nodes in node:
            results.append(nodes)
        return results

def canton_search_pathtrak_api(user_input):
    url = canton_search_link + user_input
    get_data = requests.get(url, "accept: application/json", verify=False)
    return get_data.json()
