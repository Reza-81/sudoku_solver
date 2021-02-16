import pygame
pygame.init()
#matrix
matrix=[]
for i in range(9):
    matrix+=[[]] 
    x=input()
    for j in x:    
        matrix[i]+=[j]
#base
white=(255,255,255)
blue = (52,186,230)
blac=(0,0,0)
red=(255,0,0)
yellow=(255,255,38)
green=(43,249,53)
size=(1200,900)
surface = pygame.display.set_mode(size)
surface.fill(white)

#show input
i=0
for y in range(67,834,90):   
    j=0
    for x in range(188,1013,100):        
        if matrix[i][j]=='?':
            rect = pygame.Rect(x-35,y-19,99,89)
            pygame.draw.rect(surface, white, rect)
            font = pygame.font.SysFont("Times new Roman",50)
            text=font.render(matrix[i][j],True,red)
            surface.blit(text,(x+1,y-3))
        else:
            rect = pygame.Rect(x-35,y-19,99,89)
            pygame.draw.rect(surface, blue, rect)
            font = pygame.font.SysFont("Times new Roman",30)
            text=font.render(matrix[i][j],True,blac)
            surface.blit(text,(x+5,y+5))
        if j<8:
            j+=1
    if i<8:
        i+=1


############################################################################################
#solving the soduco
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
    if t>0:    
        matrix=posible_number(matrix)
    if t>1:
        matrix=naked_single(matrix)
    if t>2:
        matrix=hiden_single(matrix)
    if t>3:
        matrix=naked_pair(matrix)
    if t>4:
        matrix=hiden_pair(matrix)
    return matrix


###############################################################################################


#counter in the update function
t=1


while True:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key== pygame.K_ESCAPE): 
            exit(0)
            break
        if event.type == pygame.KEYDOWN and event.key== pygame.K_DOWN:
            #show output
            t+=1   
            matrix=updat(matrix)
            i=0
            for y in range(67,834,90):   
                j=0
                for x in range(188,1013,100):        
                    if len(matrix[i][j])!=1:
                        rect = pygame.Rect(x-35,y-19,99,89)
                        pygame.draw.rect(surface, yellow, rect)
                        
                        for k in matrix[i][j]:
                            index=int(k)-1
                            if index in [0,1,2]:
                                temp1=0
                            elif index in [3,4,5]:
                                temp1=1
                            elif index in [6,7,8]:
                                temp1=2
                            if index in [0,3,6]:
                                temp2=0
                            elif index in [1,4,7]:
                                temp2=1
                            elif index in [2,5,8]:
                                temp2=2
                            font = pygame.font.SysFont("Times new Roman",20)
                            text=font.render(k,True,blac)
                            surface.blit(text,((x-15,x+10,x+35)[temp2],(y-10,y+15,y+40)[temp1]))
                    else:
                        font = pygame.font.SysFont("Times new Roman",30)
                        rect = pygame.Rect(x-35,y-19,99,89)
                        pygame.draw.rect(surface,green, rect)
                        text=font.render(matrix[i][j],True,blac)
                        surface.blit(text,(x+5,y+5))
                    if j<8:
                        j+=1
                if i<8:
                    i+=1
        #jadval
        width=2
        for x in range(250,1049,100):
            pygame.draw.line(surface,blac,(x,48),(x,856),width)
            if x in [350,650]:
                width=5
            else:
                width=2
        for y in range(135,850,90):
            if y in [315,585]:
                width=5
            else:
                width=2
            pygame.draw.line(surface,blac,(153,y),(1050,y),width)
        pygame.display.flip()  

