def max_integer(my_list=[]):
        if len(my_list) == 0:
                    return None

                    # On suppose que le premier nombre est le plus grand
                        largest = my_list[0]

                            # On vérifie chaque nombre dans la liste
                                for number in my_list:
                                            # Si on trouve un nombre plus grand, on le remplace
                                                    if number > largest:
                                                                    largest = number

                                                                        return largest

