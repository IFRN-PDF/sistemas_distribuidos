import random
import threading
import time

vetor_size = int(input('informe o tamanho do vetor: '))
thread_size = int(input('informe a quantidade de threads: '))
print("criando o vetor...")
list_int = list()
for i in range(vetor_size):
  list_int.append(1)

aux_thread = []

def soma(id,start , end):
  print('thread ',id,' start ',start, ' end ',end)
  soma = 0
  for i in range(start, end):
    soma += list_int[i]
  aux_thread.append(soma)
  #aux_thread.append(sum(list_int[start:end]))

thread_list = list()

for i in range(thread_size):
    start = i       * (vetor_size/thread_size)
    end   =(i + 1 ) * (vetor_size/thread_size)
      
    t = threading.Thread(target=soma, args=(i,int(start),int(end)))
    thread_list.append(t)

print("rodando threads...")
s = time.time()
for t in thread_list:
  t.start()
  
for t in thread_list:
  t.join()
e = time.time()

print("")
print('Tempo de threads ', (e-s))
print('soma de cada thread ', aux_thread)
print('soma do vetor', sum(aux_thread))

print("rodando sequencial...")
s = time.time()
#seq_sum = sum(list_int)
seq_sum = 0
for i in range(vetor_size):
    seq_sum += list_int[i]
e = time.time()

print('Tempo sequencial ', (e-s))

print('soma do vetor sequencial', seq_sum)
