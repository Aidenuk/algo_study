calculated = {}

def show_pow(x,y):
    value_key = f"{x}^{y}"
    
    def pow(x, y):
        calculated[value_key] = x ** y
        print("CALCULATING....")
        return calculated[value_key]
    

    if value_key in calculated:
        print("CALLED FROM CACHE")
        return calculated[value_key]
    else:
        pow(x, y)

show_pow(2,3)
show_pow(3,2)
show_pow(2,3)
show_pow(4,12)
show_pow(11,3)