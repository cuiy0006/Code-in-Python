from food import Food

class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a food item,
        and a reference to the next spot.
    """
    __slots__ = ("item","link")

    def __init__(self, name, next=None):
        """
        Construct a KebabSpot instance.
        :param item: the item (Food) to store at this spot
        :param next: the next KebabSpot on the skewer
        """

        self.item = Food(name)
        self.link = next


    def size(self):
        """
        Return the number of elements from this KebabSpot instance to the end
        of the skewer.
        :return: the number of elements (int)
        """
        count = 1
        temp_link = self.link
        while temp_link is not None:
            temp_link = temp_link.link
            count +=1
        return count

        # count = 0
        # temp_link = self
        # while temp_link is not None:
        #     temp_link = temp_link.link
        #     count += 1
        # return count



    def is_vegan(self):
        """
        Return whether there are all vegetables from this spot to the end of
        the skewer.
        :return True if there are no vegetables from this spot down,
        False otherwise.
        """

        temp_link = self
        while temp_link is not None:
            if not temp_link.item.is_veg:
                return False
            temp_link = temp_link.link
        return True

    def has(self, name):
        """
        Return whether there are any vegetable from this spot to the end of
        the skewer.
        :param name: the name (string) being searched for.
        :return True if any of the spots hold a Food item that equals the
        name, False otherwise.
        """

        temp_link = self
        while temp_link is not None:
            if temp_link.item.name == name:
                return True
            temp_link = temp_link.link
        return False


    def string_em(self):
        """
        Return a string that contains the list of items in the skewer from
        this spot down, with a comma after each entry.
        :return A string containing the names of each of the Food items from
        this spot down.
        """
        temp_link = self.link
        result = self.item.name
        while temp_link is not None:
            result += ',' + temp_link.item.name
            temp_link = temp_link.link
        return result

        # temp_link = self
        # lst = []
        # while temp_link is not None:
        #     lst.append(temp_link.item.name)
        #     temp_link = temp_link.link
        # return ','.join(lst)
    def get_item(self):
        return self.item
