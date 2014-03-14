import fileinput
import re
import time
from numpy import array, zeros


def calcula_m(a11, a12, a21, a22, b11, b12, b21, b22):

    m1 = strassen(a11+a22, b11+b22)
    m2 = strassen(a21+a22, b11)
    m3 = strassen(a11, b12-b22)
    m4 = strassen(a22, b21-b11)
    m5 = strassen(a11+a12, b22)
    m6 = strassen(a21-a11, b11+b12)
    m7 = strassen(a12-a22, b21+b22)

    return m1,m2,m3,m4,m5,m6,m7

def calcula_c(m1,m2,m3,m4,m5,m6,m7):
    return array([
        [m1+m4-m5+m7, m3+m5],
        [m2+m4, m1-m2+m3+m6]
    ])

def calcula_base(a11, a12, a21, a22, b11, b12, b21, b22):
    return [[a11 * b11 + a12 * b21, a11 * b12 + a12 * b22], [a21 * b11 + a22 * b21, a21 * b12 + a22 * b22]]


def strassen(a, b):
    a = array(a)
    b = array(b)
    ra, ca = a.shape
    rb, cb = b.shape
    dim = max([ra,rb,ca,cb])

    n = 1
    while n<dim:
        if dim % 2 == 0:
            break
        n += 1
        dim = 2**n

    d = dim/2

    if d == 1:
        return array([
            [a[0,0]*b[0,0] + a[0,1]*b[1,0], a[0,0]*b[0,1] + a[0,1]*b[1,1]],
            [a[1,0]*b[0,0] + a[1,1]*b[1,0], a[1,0]*b[0,1] + a[1,1]*b[1,1]]
        ])

    #Redimensionando as matrizes preenchendo com zero e tranformando em quadrada
    a11 = zeros((d, d))
    a12 = zeros((d, d))
    a21 = zeros((d, d))
    a22 = zeros((d, d))

    b11 = zeros((d, d))
    b12 = zeros((d, d))
    b21 = zeros((d, d))
    b22 = zeros((d, d))

    a11[:, :] = a[:d, :d]
    a12[:d, :ca-d+1] = a[:d, d:ca]
    a21[:ra-d+1, :] = a[d:ra-d+1, :d]
    a22[:ra-d+1, :ca-d+1] = a[d:ra-d+1, d:ca-d+1]

    b11[:, :] = b[:d, :d]
    b12[:d, :cb-d+1] = b[:d, d:cb]
    b21[:rb-d+1, :] = b[d:rb-d+1, :d]
    b22[:rb-d+1, :cb-d+1] = b[d:rb-d+1, d:cb-d+1]

    aa = [a11, a12, a21, a22, b11, b12, b21, b22]
    m1,m2,m3,m4,m5,m6,m7 = calcula_m(*aa)
    return calcula_c(m1,m2,m3,m4,m5,m6,m7)

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