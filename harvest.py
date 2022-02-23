############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

       

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)
        

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        

        

def make_melon_types():
    """Returns a list of current melon types."""
    all_melon_types = []

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing("mint")
    all_melon_types.append(musk)

    cas = MelonType("cas", 2003, "orange", False, False, "Casaba")
    cas.add_pairing("strawberries")
    cas.add_pairing("mint")
    all_melon_types.append(cas)

    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    yw = MelonType("yw", 2013, "yelow", False, True, "Yelow Wattermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)

    return all_melon_types
  
    


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
   
    for melon in melon_types:
        
        print (f"{melon.name} is pairing with:")
        for pairing in melon.pairings:
            print (f"{pairing}")
        print()



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    dict_melon_type = {}

    for melon in melon_types:
        dict_melon_type[melon.code] = melon.name

    return(dict_melon_type)

melon_types = make_melon_types()
print_pairing_info(melon_types)
melons_by_code = make_melon_type_lookup(melon_types)
print(melons_by_code)



############
# Part 2   #
############

class Melon_Harvest:
    """A melon in a melon harvest."""

    def __init__(
        self, type, shape, color, field, harvested_by
    ):
        """Initialize a melon."""
       
        self.type = type
        self.shape = shape
        self.color = color
        self.field = field
        self.harvested_by = harvested_by
        self.sellable = False

    def is_sellable(self, color, shape, field): 
            if self.color >= 5 and self.shape >= 5 and field != 3:
                self.sellable = True
            return self.sellable


        

def make_melons():
    """Returns a list of Melon objects."""

    all_melons = []
    
    melon1 = Melon_Harvest("yw", 8, 7, 2, "Sheila")
    melon1.is_sellable(melon1.color, melon1.shape, melon1.field)
    all_melons.append(melon1)

    melon2 = Melon_Harvest("yw", 3, 4, 2, "Sheila")
    melon2.is_sellable(melon2.color, melon2.shape, melon2.field)
    all_melons.append(melon2)

    melon3 = Melon_Harvest("yw", 9, 8, 3, "Sheila")
    melon3.is_sellable(melon3.color, melon3.shape, melon3.field)
    all_melons.append(melon3)

    melon4 = Melon_Harvest("cas", 10, 6, 35, "Sheila")
    melon4.is_sellable(melon4.color, melon4.shape, melon4.field)
    all_melons.append(melon4)

    melon5 = Melon_Harvest("cren", 8, 9, 35, "Michael")
    melon5.is_sellable(melon5.color, melon5.shape, melon5.field)
    all_melons.append(melon5)

    melon6 = Melon_Harvest("cren", 8, 2, 35, "Michael")
    melon6.is_sellable(melon6.color, melon6.shape, melon6.field)
    all_melons.append(melon6)

    melon7 = Melon_Harvest("cren", 2, 3, 4, "Michael")
    melon7.is_sellable(melon7.color, melon7.shape, melon7.field)
    all_melons.append(melon7)

    melon8 = Melon_Harvest("musk", 6, 7, 4, "Michael")
    melon8.is_sellable(melon8.color, melon8.shape, melon8.field)
    all_melons.append(melon8)

    melon9 = Melon_Harvest("yw", 7, 10, 3, "Sheila")
    melon9.is_sellable(melon9.color, melon9.shape, melon9.field)
    all_melons.append(melon9)

    return all_melons




def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:

        if melon.sellable == True:
            print(f"Harvested by {melon.harvested_by} from Field {melon.field} (CAN BE SOLD)")

        else:
            print(f"Harvested by {melon.harvested_by} from Field {melon.field} (NOT SELLABLE)")


melons = make_melons()
print()
get_sellability_report(melons)

