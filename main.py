import fileinput
import re
import time

def calcula_m(a11, a12, a21, a22, b11, b12, b21, b22):

    m1 = (a11+a22)*(b11+b22)
    m2 = (a21+a22)*b11
    m3 = a11*(b12-b22)
    m4 = a22*(b21-b11)
    m5 = (a11+a12)*b22
    m6 = (a21-a11)*(b11+b12)
    m7 = (a12-a22)*(b21+b22)

    return m1,m2,m3,m4,m5,m6,m7

def calcula_c(m1,m2,m3,m4,m5,m6,m7):
    c11 = m1+m4-m5+m7
    c12 = m3+m5
    c21 = m2+m4
    c22 = m1-m2+m3+m6

    return c11,c12,c21,c22

def strassen(a, b):
    ra,rb = len(a),len(b)
    ca,cb = len(a[0]) or 0,len(b[0]) or 0
    dim = max([ra,rb,ca,cb])

    n = 1
    while n<dim:
        if dim % 2 == 0:
            break
        n += 1
        dim = 2**n

    d = dim/2

    #Redimensionando as matrizes preenchendo com zero e tranformando em quadrada
    a11 = [[0 for j in xrange(0, d)] for i in xrange(0, d)]
    a12 = [[0 for j in xrange(0, d)] for i in xrange(0, d)]
    a21 = [[0 for j in xrange(0, d)] for i in xrange(0, d)]
    a22 = [[0 for j in xrange(0, d)] for i in xrange(0, d)]

    b11 = [[0 for j in xrange(0, d)] for i in xrange(0, d)]
    b12 = [[0 for j in xrange(0, d)] for i in xrange(0, d)]
    b21 = [[0 for j in xrange(0, d)] for i in xrange(0, d)]
    b22 = [[0 for j in xrange(0, d)] for i in xrange(0, d)]


    for i in xrange(0, d):
        for j in xrange(0, d):
            a11[i][j] = a[i][j]
            a12[i][j] = a[i][j + d]
            a21[i][j] = a[i + d][j]
            a22[i][j] = a[i + d][j + d]

            b11[i][j] = b[i][j]
            b12[i][j] = b[i][j + d]
            b21[i][j] = b[i + d][j]
            b22[i][j] = b[i + d][j + d]


    if dim == 1:
        return [ a11*b11 + a12*b21 , a11*b12+a12*b22], [ a21*b11+a22*b21, a21*b12+a22*b22]
    elif dim == 2:
        aa = [a11[0][0], a12[0][0], a21[0][0], a22[0][0], b11[0][0], b12[0][0], b21[0][0], b22[0][0]]
        m1,m2,m3,m4,m5,m6,m7 = calcula_m(*aa)
        c11,c12,c21,c22 = calcula_c(m1,m2,m3,m4,m5,m6,m7)
        c = [[c11,c12],[c21,c22]]

    else:
        c11 = strassen(a11,b11)
        c12 = strassen(a12,b12)
        c21 = strassen(a21,b21)
        c22 = strassen(a22,b22)

        c = [[c11, c12], [ c21, c22]]
    return c

def clear_and_convert_to_int(line):
    line = re.findall("\d+" , line)
    line = map(lambda x: int(x), line)
    return line

def execute():
    if not fileinput.input():
        print "Ta de pegadinha? Input vazio..."
    else:
        a = []
        b = []
        jump = False
        for line in fileinput.input():
            if line == '\n':
                jump = True
            if not jump:
                a.append(clear_and_convert_to_int(line))
            else:
                b.append(clear_and_convert_to_int(line))
        b.pop(0)



        print strassen(a,b)



if __name__ == "__main__":
        end = time.time()
        execute()
        start = time.time()
        print "Tempo de execucao: ", end-start