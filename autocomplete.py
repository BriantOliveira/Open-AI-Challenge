def extract(query):
    """extract takes in a `query` API function (which returns the first 5 usernames, lexicographically sorted,
    that start with a prefix) and returns the sorted list of all usernames in the database.

    For example, the `query` function in provided in `main` works as follows:

    query("a") #=> ["abracadara", "al", "alice", "alicia", "allen"]
    query("ab") #=> ["abracadara"]

    The following implementation would pass the assertion in `main`, but is not a correct solution since it
    works only for that example `query`:

    def extract(query):
        return query("ab") + query("al") + query("altercation") + query("b") + query("el") + query("ev") + query("m")

    Your goal is to write an `extract` method that is correct for any provided `query`.
    """
    # YOUR CODE HERE

    # Start with 5 words
    # Store every word queried
    Data = []
    def autocomplete(string = None):
        #Starting the first search
        if not string:
            given_query = query("a")
            Data.extend(given_query)
            #Searching recursively with the last word query
            return autocomplete(Data[-1])
        #After the initial search
        else:
            given_query = query(string)
            # If there is not any new words
            if len(given_query) == 1:
                # Increment letters until the new word is found
                while True:
                    # Increase the last letter a -> b
                    last_letter = chr(ord(string[-1]) + 1)
                    # Modify the string bob to boc
                    string = string[0:len(string) - 1] + last_letter
                    # Query with the new word
                    new_query = query(string)
                    # Found the new word
                    if len(new_query) > 0:
                        # Get the new words
                        new_words = []
                        for word in new_query:
                            if word not in Data:
                                new_words.append(word)
                        # Add the new word to the Data
                        Data.extend(new_words)
                        # The search continues from the new word
                        autocomplete(Data[-1])
                    #If the last letter goes over z
                    elif ord(last_letter) == 123:
                        #Remove the last letter
                        string = string[0:len(string) - 1]
                        # If there is nothing more, return the whole Data
                        if not string:
                            return Data
            else:
                # Add the newest words to Data
                new_words = given_query[1:len(given_query)]
                Data.extend(new_words)
                #Search from the newest word
                autocomplete(Data[-1])

    return autocomplete()


def main():
    """Runs your solution -- no need to update (except to maybe try out different databases)."""
    # Sample implementation of the autocomplete API
    # database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve", "evening", "event", "eventually", "mallory"]
    database = ["alec", "alef", "alep", "briant", "brianna", "bright", "ester", "esus", "max", "navy", "orney", "peter", "quanty", "ross", "rossa", "tattoo", "tatu", "zayne" ]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database
    if extract(query) == database:
        print("Oh yeahhh! OpenAI here I come :)")

main()
