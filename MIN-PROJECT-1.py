from collections import deque
import collections
 
def solver(start,end,dictionary):
    
    queue=deque()
    #using deque, since it as a double linked list, it is more efficient.
    queue.append((start,[start]))
    
    while queue:
       
        node,path=queue.popleft()
        print('visit node*************',node)   
        print('current transformation count:',len(path))
        
        print('visited path=',path) 
         
        for next in get_successor(node,dictionary)-set(path):
          #get the possible successor and subtract the already visited one in the selected path
            if next==end:
                path=path+[end]
                print('found end at the path:',path)
                return len(path)
            else:
            
                queue.append((next,path+[next]))
             
    return 0 
   
def get_successor(parent, dictionary):
    #this functiom to get the possible successor from the previous word.
    #the successor which has a character different with the parents
  if (parent in dictionary):
    dictionary.remove(parent)

  possiblenodes=set()
  for word in dictionary:
    different=0
    for index in range(len(word)):
      
      if (word[index]!=parent[index]):
          different+=1
      #when list character has one different letter with start
      #append it into wordlist.
    if(different==1):
        possiblenodes.add(word)
       
  
  return possiblenodes


start='boy'
end='cup'
dictionary=['try','toy','cop','cup','coy',
            'fry','cry','bay','lay','boy',
            'bow','fey']

print(solver(start,end,dictionary))
