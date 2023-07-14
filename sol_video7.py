#Mostrar la tabla de verdad de la expresión (A o Falso) y (B o Negado B)
A=True; B=True
print("  A   |     B  | A o False | B o negado B | (A o Falso) y (B o Negado B)") 
print(A," | " , B, " | ", A or False , "| " , B or not B ,"|",(A or False) and (B or not B))
print(A," | " , not B, " | ", A or False , "| " , not B or not(not B),"|",(A or False) and (not B or not(not B)))
print(not A," | " , B, " | ", not A or False , "| " , B or not B,"|",(not A or False) and (B or not B))
print(not A," | " , not B, " | ", not A or False , "| " , not B or not(not B),"|",(not A or False) and (not B or not(not B)))