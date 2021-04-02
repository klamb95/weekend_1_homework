# WRITE YOUR FUNCTIONS HERE
   
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop['admin']['total_cash'] += cash
    return pet_shop['admin']['total_cash']

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']

def increase_pets_sold(pet_shop, pets):
    pet_shop['admin']['pets_sold'] += pets
    return pet_shop['admin']['pets_sold']

def get_stock_count(pet_shop):
    return len(pet_shop['pets'])
    


    







   
        






    