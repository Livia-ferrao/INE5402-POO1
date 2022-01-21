cVit, cEmp, cGols, fVit, fEmp, fGols = input().split()
cVit, cEmp, cGols, fVit, fEmp, fGols = int(cVit), int(cEmp), int(cGols), int(fVit), int(fEmp), int(fGols)

golsC = cVit*3 + cEmp*1
golsF = fVit*3 + fEmp*1

if golsC > golsF:
    print("C")
    
elif golsF > golsC: 
    print("F")
    
elif golsC == golsF:
    if cGols> fGols:
        print("C")
    elif fGols > cGols:
        print("F")
    elif fGols == cGols:
        print("=")
    