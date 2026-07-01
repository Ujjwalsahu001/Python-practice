class dietplan:
    def get_breakfast(self):
        pass

class ketodiet(dietplan):
    def get_breakfast(self):
        return "eggs,avacado,bacon fried"


class vegandiet(dietplan):
    def get_breakfast(self):
        return "oatmeal with milk,chia seeds"
    
class highprotiendiet(dietplan):
    def get_breakfast(self):
        return "greek yogcurt, a banana"
    
def print_morning_routine(diet_object):
    print(f"Today's Breakfast: {diet_object.get_breakfast()}")

#create instances
my_keto = ketodiet()
my_vegan = vegandiet()
my_protein = highprotiendiet()

print_morning_routine(my_keto)
print_morning_routine(my_vegan)
print_morning_routine(my_protein)