# Altura y rebote : 

print("---------------------------")
print("--- ALTURA - Y - REBOTE ---")
print("---------------------------")

# Input
H = int(input("Digite el valor de la altura: "))

#Processing
i = 0
R = H
while R > H*0.2:
    R = R - R * 0.1
    i = i + 1

#Output
print(i)
