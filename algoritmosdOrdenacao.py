
def bubble_sort(array:list):
    for numero in range(len(array)-1,0,-1):
      for index in range(numero):
       if array[index] > array[index+1]:
        tempo = array[index]
        array[index] = array[index+1]
        array[index + 1] = tempo

# modificação feita no clone na maquina local

def insertion_sort(array:list):
     for index in range(1,len(array)):
        valorAtual = array[index]
        posicao = index
        while posicao >0 and array[posicao-1]>valorAtual:
          array[posicao] = array[posicao-1]
          posicao = posicao-1

        array[posicao]= valorAtual