seq ="CGATGATGAATTCGTACCCGAGCTGAATTCAGCAGAATTCAGCTGATCGATACCAGAATTCCATA"
ecoRI = "GAATTC"
def ecor1(enzima, seq):
    sitios_corte = []
    seq_copy = seq  
    
    while True:
        sitiocorte = seq_copy.find(enzima)
        if sitiocorte == -1:
            break
        frag1 = seq_copy[:sitiocorte + len(enzima)]
        frag2 = seq_copy[sitiocorte + len(enzima):]
        sitios_corte.append(frag1)
        seq_copy = frag2
    
    sitios_corte.append(seq_copy)  
    
    return sitios_corte

resultados = ecor1(ecoRI, seq)
print(resultados)
