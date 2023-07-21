from worksheet import get_dictionary, add_element, loop_keys, loop_elements, get_length
import time


def main():
    d = get_dictionary()
    print("Greetings employee number 23068. Your functions are now running...")
    time.sleep(1)

    try:
        d = add_element(d)
        assert 'metachlorians' in d
        print("add_element() function passed! Keep it up!")
    except:
        print("add_element() function failed. Make sure you add metachlorians as a key with a value of '20000'.")
        time.sleep(0.1)
        print("Self-destructing in 3, 2, 1...")
        return

    time.sleep(1)
    try:
        d_length = get_length(d)
        assert d_length == 14
        print("get_length() function passed! New T-shirt unlocked!")
    except:
        print("get_length() function failed. Hint: the length is 14. Is there a built-in Python `length` function that can help you check this?")
        return

    time.sleep(1)
    try:
        d_key_list = loop_keys(d)
        assert d_key_list == ['birth_year', 'eye_color', 'films', 'gender', 'hair_color', 'height',
                              'homeworld', 'mass', 'name', 'skin_color', 'created', 'edited', 'url', 'metachlorians']
        print("loop_keys() function passed! You, sir, are a scholar.")
    except:
        print("Ruh roh. loop_keys() function failed. Inside of the loop, add each key to the list of keys. \nYou can do this using Python's list.append() function.")
        return

    time.sleep(1)
    try:
        d_element_list = loop_elements(d)
        assert d_element_list == ['birth_year -> 19 BBY', 'eye_color -> Blue', "films -> ['https://swapi.dev/api/films/1/', 'https://swapi.dev/api/films/2/', 'https://swapi.dev/api/films/3/']", 'gender -> Male', 'hair_color -> Blond', 'height -> 172',
                                  'homeworld -> https://swapi.dev/api/planets/1/', 'mass -> 77', 'name -> Luke Skywalker', 'skin_color -> Fair', 'created -> 2014-12-09T13:50:51.644000Z', 'edited -> 2014-12-10T13:52:43.172000Z', 'url -> https://swapi.dev/api/people/1/', 'metachlorians -> 20000']
        print("loop_elements() function passed! By golly you've done it again.")
    except:
        print("loop_elements() function failed. Inside of the loop, add the key and its value to each item of the list. Python's string literals can help you accomplish this.")
        return

    time.sleep(1)
    print("============================")
    print("All tests passed. NICE WORK!!")


if __name__ == '__main__':
    main()
