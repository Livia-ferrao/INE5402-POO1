codigo, qntd = input().split()
codigo = int(codigo)
qntd = int(qntd)
if codigo == 1:
    total = 4.00 * qntd
if codigo == 2:
    total = 4.50 * qntd
if codigo == 3:
    total = 5.00 * qntd
if codigo == 4:
    total = 2.00 * qntd
if codigo == 5:
    total = 1.50 * qntd
    
print("Total: R$ %.2f" % total)