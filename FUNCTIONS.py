def MATRIX(rows,columns):
    original_matrix=[]
    sorted_matrix=[]
    adduct_matrix=[]
    # input the matrix 
    for a in range (rows):
        c=[]
        q=[]
        for b in range (columns):
            d=int(input(f"Enter element {a+1},{b+1} : "))
            c.append(d)
            q.append(d)
        original_matrix.append(q)
        # create a bubble sort for the matrix
        g=len(c)
        for i in range (g):
            for j in range (0,g-i-1):
                if c[j]>c[j+1]:
                    c[j],c[j+1]=c[j+1],c[j]
        sorted_matrix.append(c)
    # print the original matrix 
    print("The Original Matrix is : ")
    for e in range (rows):
        for f in range (columns):
            print(original_matrix[e][f],end=" ")
        print()
    # print the sorted matrix 
    print("The Sorted Matrix is : ")
    for h in range (rows):
        for k in range (columns):
            print(sorted_matrix[h][k],end=" ")
        print()
    # add the original and sorted matrix
    for l in range (rows):
        n=[]
        for m in range (columns):
                n.append(original_matrix[l][m]+sorted_matrix[l][m])
        adduct_matrix.append(n)
    # print the adduct matrix
    print("The Adduct Matrix is : ")
    for o in range (rows):
        for p in range (columns):
            print(adduct_matrix[o][p],end=" ")
        print()
# function call
MATRIX(2,2)

def BUBBLE_SORT (r):
    # BUBBLE SORT
    m=[]
    for i in range (r):
        a=int(input(f"Enter element {i+1} : "))
        m.append(a)
    n=len(m)
    for i in range (n):
        for j in range (0,n-i-1):
            if m[j]>m[j+1]:
                m[j],m[j+1]=m[j+1],m[j]
    print(m)
