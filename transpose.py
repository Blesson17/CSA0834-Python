rows=int(input("enter the number of rows"))
column=int(input("enter the number of column"))
print("enter the matrix elements")
matrix=[[int(input())for i in range(column)]for j in range(rows)]
print("matrix elements:")
for i in range(rows):
    for j in range(column):
        print(forms(matrix[i][j],"<5"),end="")
        print()  
result=[[int(0)for i in range(rows)]for j in range(column)]
print("Transpose matrix:")
for i in range(column):
    for j in range(rows):
        result[i][j]=matrix[j][i]
        print(form(result[i][j],"<5"),end="")
    print()
