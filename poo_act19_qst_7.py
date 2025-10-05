# Act 19 :
# Qst 7 :
def F7(n):
    if n == 0 or n==1 :
        return n
    return F7(n-1)+F7(n-2)
    
n = int(input("Entrer le n-eme terme : "))
print(F7(n))

# Nom Complet : WAEL BOUHAYA
# Filière : IAGI-1 


