adict = {
    19: 19.49,    
    21: 19.16,
    14: 5.99,
}
def func():
    for key, value in adict.items():
        q = (key)**-1*(1.2e-14)/((value*(1+1.64e-2*(value**0.5)))**1.5)
        print(q)

func()
