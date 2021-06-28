import subprocess

def remove_spaces(table,rows,cols):
    for i in range(0,rows):
        for j in range(0,cols):
            temp = ""
            for s in table[i][j]:
                if(s != ' '): temp += s
            table[i][j] = temp
    return table


def create_table(table,o,rows,cols):

    j = 0
    i = 0

    #In case the value of that column doesnot start with the beginning index of column header
    header_size = 0             
    k = 0
    j = 0
    while(j < len(o[0])):
        #print("           ",j)
        if(o[0][j] != ' '):
            c = 0
            t = j
            #-------Calculate the length of the column header---------
            header_size = 0                         
            while(o[0][t] != ' '):                      
                header_size +=1                         
                t += 1                                    
                if(t >= len(o[0])):                       
                   break                               
            #-------Fill each row of the table of particular column--------    
            for i in range(0,len(o)):
                m = j
                while(o[i][m] != ' ' or m < j+header_size):
                    #print(i," ",k," ",m)
                    table[i][k] = table[i][k] + str(o[i][m])
                    m = m+1
                    if(i == 0):
                        c = c+1
                    if(m >= len(o[0])):
                        break
            k = k+1
            j += c
            #print("     ",c,"  ",j)
        j+= 1
    return table


cmd = 'vgs'
sp = subprocess.Popen(cmd,shell = True,stdout = subprocess.PIPE,stderr = subprocess.PIPE
                      ,universal_newlines = True)
success_code = sp.wait()
out,err = sp.communicate()
o = out.splitlines()

if(success_code == 0):
    rows = len(o)
    cols = 7
    table = [["" for i in range(cols)] for j in range(cols)]
    table = create_table(table,o,rows,cols)
    table = remove_spaces(table,rows,cols)
    print('The physical volumes : ')
    for i in range(1,rows):
        print(table[i][0])
    print(f'Detailed properties : \n{out}')
else:
    print(f'Error.............\n{err}')
