#entradas
N=int(input("Inserte el digito "))
K=int(input("Inserte el digito"))
#caja negra 
while True:
    N=0
    if(K<N):
        N=N-1
        print(N)
    elif(N==K):
        print(K)
        break 
         