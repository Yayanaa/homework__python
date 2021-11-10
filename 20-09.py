def unique(list1):                 
    unique_list = []                                      
    i = 0                                                        
    for item in list1:                                          
        i = i + 1                                               
        if item  not in list1[i:] and item not in list1[:i-1]:  
            unique_list.append(item)                           
    return unique_list                                          

def intersection(list1, list2):                                 
    intersection_list = []                                     
    for item in list1:                                          
        if item in list2:                                       
            intersection_list.append(item)                      
    return intersection_list                                    
print(unique([1,2,2,3,4,4,5]))                                  
print(intersection([1,2,3,4,6], [1,3,4,5,2]))      
