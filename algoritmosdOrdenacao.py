
def bubble_sort(array:list):
    for numero in range(len(array)-1,0,-1):
      for index in range(numero):
       if array[index] > array[index+1]:
        tempo = array[index]
        array[index] = array[index+1]
        array[index + 1] = tempo