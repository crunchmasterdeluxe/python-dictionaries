
def get_dictionary():
    """
        A dictionary, like a json object, is an object of key-value pairs.
        Ref https://www.w3schools.com/python/python_dictionaries.asp for dictionary basics
    """
    return {
        "birth_year": "19 BBY",
        "eye_color": "Blue",
        "films": [
            "https://swapi.dev/api/films/1/",
            "https://swapi.dev/api/films/2/",
            "https://swapi.dev/api/films/3/",
        ],
        "gender": "Male",
        "hair_color": "Blond",
        "height": "172",
        "homeworld": "https://swapi.dev/api/planets/1/",
        "mass": "77",
        "name": "Luke Skywalker",
        "skin_color": "Fair",
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-10T13:52:43.172000Z",
        "url": "https://swapi.dev/api/people/1/"
    }


def add_element(d):
    """
        Add a new item to the dictionary called metachlorians with a value of 20000
    """

    # put your code here
    #####################
    d['metachlorians'] = "20000"
    #####################

    return d


def get_length(d):
    """
        Create a variable named `d_length` that is assigned the integer length of the dictionary 
        (how many items does it contain?)
    """

    # put your code here
    #####################
    d_length = len(d)
    #####################

    return d_length


def loop_keys(d):
    """
        Loop through the dictionary and add (append) each the key to a list named key_list
    """

    key_list = []
    # put your code here
    #####################
    for i in d:
        key_list.append(i)
    #####################

    return key_list


def loop_elements(d):
    """
        Loop through the dictionary and add (append) each key and its value to a list named element_list.
        Add the key-value pairs in this format: `key "->" value`
    """

    element_list = []
    # put your code here
    #####################
    for i in d:
        element_list.append("{} -> {}".format(i, d[i]))
    #####################

    return element_list
