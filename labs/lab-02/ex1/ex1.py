import time

def do_append(size):
  result = [None for i in range(size)]
  for i in range(size):
    message= "some unique object %d" % ( i, ) * 1000
    result[i] = message
    time.sleep(0.0001)
  return result

def do_allocate(size):
  result=size*[None]
  for i in range(size):
    message= "some unique object %d" % ( i, ) * 1000
    result[i]= message
    time.sleep(0.0001)            
  return result


if __name__ == '__main__':
  size = 10000000
  
  #
  # Experiment 1 
  #
  # do_append(size)
  
  #
  # Experiment 2
  #
  do_allocate(size)
  print("DONE allocate")

  # 
  # Experiment 3
  #
  # do_append(size)
  # print("DONE append")
  # do_allocate(size)

  #
  # Experiment 4
  #
  #result1 = do_append(size)
  #result2 = do_allocate(size)
