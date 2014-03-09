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
    ca,cb = len(a[0]),len(b[0])
    dim = max([ra,rb,ca,cb])


    #TODO - Criar formar de achar potencia de 2 mais proxima, evitando matrizes impares

    #TODO - Criar metodo para redimensionar preenchendo de zero os espacos vazios

    a11 = a[0:dim/2][0:dim/2]
    a12 = a[0:dim/2][dim/2+1:]
    a21 = a[dim/2+1:][0:dim/2]
    a22 = a[dim/2+1:][dim/2+1:]

    b11 = b[0:dim/2][0:dim/2]
    b12 = b[0:dim/2][dim/2+1:]
    b21 = b[dim/2+1:][0:dim/2]
    b22 = b[dim/2+1:][dim/2+1:]


    dimensao = 0 #calcula_dim(a,b)
    c = None

    if dimensao == 1:
        return [ a11*b11 + a12*b21 , a11*b12+a12*b22], [ a21*b11+a22*b21, a21*b12+a22*b22]
    elif dimensao == 2:
        # input_m = a11, a12, a21, a22, b11, b12, b21, b22
        m = calcula_m(a11, a12, a21, a22, b11, b12, b21, b22)
        c = 0 #calcula_c(m)

    else:
        c11 = strassen(a11,b11)
        c12 = strassen(a12,b12)
        c21 = strassen(a21,b21)
        c22 = strassen(a22,b22)

        c = [[c11, c12], [ c21, c22]]
    return c






if __name__ == "__main__":
        end = time.time()

        #Executa aqui
        start = time.time()
        print "Tempo de execucao: ", end-start