matrix=[]
for i in range(9):
    matrix+=[[]] 
    x=input()
    for j in x:    
        matrix[i]+=[j]

for i in range(9):
    for j in range(9):
        if matrix[i][j]=='?':    
            matrix[i][j]=['1','2','3','4','5','6','7','8','9']

#creat posible number
def posible_number(matrix):
        
    for i in range(9):
        for j in range(9):
            if type(matrix[i][j])!=str:   
                
                temp=matrix[i][j][:]
                #row
                for k in temp:
                    if k in matrix[i]:
                        matrix[i][j].remove(k)
                
                temp=matrix[i][j][:]
                #column
                for x in range(9):
                    for k in temp:
                        if k == matrix[x][j]:
                            matrix[i][j].remove(k)
                
                temp=matrix[i][j][:]
                #bloc
                for x in range((i//3)*3,(i//3)*3+3):
                    for y in range((j//3)*3,(j//3)*3+3):
                        for k in temp:
                            if k==matrix[x][y]:
                                matrix[i][j].remove(k)
    return matrix

#naked single
def naked_single(new_matrix):
    flag=False
    for i in range(9):
        for j in range(9):
            if len(new_matrix[i][j])==1:
                if new_matrix[i][j]!=new_matrix[i][j][0]:
                    flag=True
                    new_matrix[i][j]=new_matrix[i][j][0]
    if flag:
        new_matrix=posible_number(new_matrix)
        new_matrix=naked_single(new_matrix)
        return new_matrix
    else:
        return new_matrix

#hiden single
def hiden_single(new_matrix):
    #row
    for i in range(9):
        for j in range(9):
            if type(new_matrix[i][j])==list:
                for k in new_matrix[i][j]:
                    flag=0
                    for z in range(9):
                        if type(new_matrix[i][z])==list:
                            if k in new_matrix[i][z]:
                                flag+=1
                                if flag>1:    
                                    break
                    if flag==1:
                        new_matrix[i][j]=k
                        new_matrix=posible_number(new_matrix)
                        new_matrix=naked_single(new_matrix)
                        new_matrix=hiden_single(new_matrix)
                        break
                        #return new_matrix
    
    #column
    for i in range(9):
        for j in range(9):
            if type(new_matrix[i][j])==list:
                for k in new_matrix[i][j]:
                    flag=0
                    for z in range(9):
                        if type(new_matrix[z][j])==list:
                            if k in new_matrix[z][j]:
                                flag+=1
                                if flag>1:
                                    break
                    if flag==1:
                        new_matrix[i][j]=k
                        new_matrix=posible_number(new_matrix)
                        new_matrix=naked_single(new_matrix)
                        new_matrix=hiden_single(new_matrix)
                        break
                        #return new_matrix
    
    #bloc
    for i in range(9):
        for j in range(9):        
            if type(new_matrix[i][j])==list:        
                for k in matrix[i][j]:
                    flag=0
                    for x in range((i//3)*3,(i//3)*3+3):
                        for y in range((j//3)*3,(j//3)*3+3):
                            if type(new_matrix[x][y])==list:
                                if k in new_matrix[x][y]:
                                    flag+=1
                                    if flag>1:
                                        break
                    if flag==1:
                        new_matrix[i][j]=k
                        new_matrix=posible_number(new_matrix)
                        new_matrix=naked_single(new_matrix)
                        new_matrix=hiden_single(new_matrix)
                        break
                        #return new_matrix            
    return new_matrix

#naked pair
def delet(new_matrix,i,j,s1,s2,RCB):
    #row
    if RCB=='row':
        for k in new_matrix[i][j]:
            for z in range(9):
                if z!=j and z!=s2 and k in new_matrix[i][z] and type(new_matrix[i][z])==list:
                    new_matrix[i][z].remove(k)
        return new_matrix
    #column
    if RCB=='column':    
        for k in new_matrix[i][j]:
            for q in range(9):
                if q!=i and q!=s1 and k in new_matrix[q][j] and type(new_matrix[q][j])==list:
                    new_matrix[q][j].remove(k)
        return new_matrix
    #bloc
    if RCB=='bloc':    
        for k in new_matrix[i][j]:
            for x in range((i//3)*3,(i//3)*3+3):
                for y in range((j//3)*3,(j//3)*3+3):
                    if (x!=i or y!=j) and (x!=s1 or y!=s2 )and k in new_matrix[x][y] and type(new_matrix[x][y])==list:
                        new_matrix[x][y].remove(k)
        return new_matrix


def naked_pair(new_matrix):
    #row
    for i in range(9):
        for j in range(9):
            if type(new_matrix[i][j])==list and len(new_matrix[i][j])==2:
                for z in range(9):
                    if z!=j:
                        if new_matrix[i][j]==new_matrix[i][z]:
                            new_matrix1=delet(new_matrix,i,j,i,z,'row')
                            new_matrix=new_matrix1
                            new_matrix=naked_single(new_matrix)
                            new_matrix=hiden_single(new_matrix)
                            new_matrix=posible_number(new_matrix)
                            if new_matrix1!=new_matrix:
                                new_matrix=naked_pair(new_matrix)
                            
    #column
    for i in range(9):
        for j in range(9):
            if type(new_matrix[i][j])==list and len(new_matrix[i][j])==2:
                for q in range(9):
                    if q!=i:
                        if new_matrix[i][j]==new_matrix[q][j]:
                            new_matrix1=delet(new_matrix,i,j,i,z,'row')
                            new_matrix=new_matrix1
                            new_matrix=naked_single(new_matrix)
                            new_matrix=hiden_single(new_matrix)
                            new_matrix=posible_number(new_matrix)
                            if new_matrix1!=new_matrix:
                                new_matrix=naked_pair(new_matrix)
                            
    #bloc
    for i in range(9):
        for j in range(9):     
             if len(new_matrix[i][j])==2:
                for x in range((i//3)*3,(i//3)*3+3):
                    for y in range((j//3)*3,(j//3)*3+3):
                        if x!=i or y!=j:
                            if new_matrix[i][j]==new_matrix[x][y]:
                                new_matrix1=delet(new_matrix,i,j,i,z,'row')
                                new_matrix=new_matrix1
                                new_matrix=naked_single(new_matrix)
                                new_matrix=hiden_single(new_matrix)
                                new_matrix=posible_number(new_matrix)
                                if new_matrix1!=new_matrix:
                                    new_matrix=naked_pair(new_matrix)
                              

    return new_matrix

#hiden pair
def intresection(new_matrix,i,j,x,y):
    temp=[]
    for k in new_matrix[i][j]:
        if k in new_matrix[x][y]:
            temp+=[k]
    return temp
    

def hiden_pair(new_matrix):
    #row
    for i in range(9):
            for j in range(9):
                if len(new_matrix[i][j])>2:
                    for y in range(9):
                        if y!=j:    
                            temp=intresection(new_matrix,i,j,i,y)
                            if len(temp)>=2:
                                lst=[]
                                for k in temp:
                                    flag1=0
                                    for z in range(9):
                                        if k in matrix[i][z] and type(matrix[i][z])==list:
                                            flag1+=1
                                    if flag1==2:
                                        lst+=[k]
                                if len(lst)==2:
                                    new_matrix[i][j],new_matrix[i][y]=lst,lst
    
    #column
    for i in range(9):
            for j in range(9):
                if len(new_matrix[i][j])>2:
                    for x in range(9):
                        if x!=i:    
                            temp=intresection(new_matrix,i,j,x,y)
                            if len(temp)>=2:
                                lst=[]
                                for k in temp:
                                    flag1=0
                                    for q in range(9):
                                        if k in matrix[q][j] and type(matrix[q][j])==list:
                                            flag1+=1
                                    if flag1==2:
                                        lst+=[k]
                                if len(lst)==2:
                                    new_matrix[i][j],new_matrix[x][j]=lst,lst
    
    #bloc
    for i in range(9):
        for j in range(9):
            if len(new_matrix[i][j])>2:
                for x in range((i//3)*3,(i//3)*3+3):
                    for y in range((j//3)*3,(j//3)*3+3):
                        if x!=i or y!=j:    
                            temp=intresection(new_matrix,i,j,x,y)
                            if len(temp)>=2:
                                lst=[]
                                for k in temp:
                                    flag1=0
                                    for q in range((i//3)*3,(i//3)*3+3):
                                        for z in range((j//3)*3,(j//3)*3+3):
                                            if k in matrix[q][z] and type(matrix[q][z])==list:
                                                flag1+=1
                                    if flag1==2:
                                        lst+=[k]
                                if len(lst)==2:
                                    new_matrix[i][j],new_matrix[x][y]=lst,lst
                                        
                                        
    return new_matrix                    


#updat
def updat(matrix):
    matrix=posible_number(matrix)
    matrix=naked_single(matrix)
    matrix=hiden_single(matrix)
    matrix=naked_pair(matrix)
    matrix=hiden_pair(matrix)
    return matrix

matrix=updat(matrix)
for i in range(9):
    for j in range(9):
        if type(matrix[i][j])!=list:    
            print(matrix[i][j],end='')
        else:
            print('?',end='')
    print()