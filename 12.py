"""
def temperatuur(temp,yhik):
    """
    See on maailma parim manual 
    Parameetric: kui ei tea, siis ei tea
    Näide: uuri ise    
    """


    if yhik == "c":
        v = temp * 5/9 + 32
    else:
        v = (temp - 32) * 5/9
    return v

print(temperatuur(3,"c"))
print(temperatuur(3,"f"))
print(temperatuur.__doc__)"""