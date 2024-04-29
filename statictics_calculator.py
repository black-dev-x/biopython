def mean(list):
  return sum(list)/len(list)
  
def median(list):
  size = len(list)
  sorted_list = sorted(list)
  if(size % 2 == 0):
    return (sorted_list[size//2] + sorted_list[(size//2) - 1]) / 2
  return sorted_list[(size // 2 ) + 1]

def mode(list):
  list_dictionary = {}
  maximum_value = 0
  maximum_element = list[0]
  for element in list:
    if element not in list_dictionary:
      list_dictionary[element] = 1
    else:
      new_value = list_dictionary[element] + 1
      list_dictionary[element] = new_value
      if(new_value > maximum_value):
        maximum_value = new_value
        maximum_element = element
      
  return maximum_element
