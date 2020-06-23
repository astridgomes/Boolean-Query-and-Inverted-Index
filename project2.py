#Code to create a postings lis
import sys
input1=sys.argv[1]
output1=sys.argv[2]
queries1=sys.argv[3]
inter_list=[]
new_dict={}
#path_of_input_corpus=open(r'C:\Users\Astrid\Documents\IR\Project2\input.txt')
path_of_input_corpus=open(input1,'r')
for each_line in path_of_input_corpus:
    #split on tab so doc id and words separate
    doc_id_words=each_line.split('\t')
    #Append to a list
    inter_list.append([doc_id_words[0],doc_id_words[1]])    
    #print(inter_list)
        
for every_term in inter_list: 
    individual_term=every_term[1].split()
    #print(individual_term)
    individual_term_new=list(dict.fromkeys(individual_term))
    #print(individual_term_new)
    #print(individual_term)
    for term in individual_term_new:
        if(new_dict.get(term)):
            new_dict[term].append(every_term[0])
        else:
            new_dict[term]=[every_term[0]]
list1 = [(k, v) for k, v in new_dict.items()] 

#path_of_output_result = open('C:/Users/Astrid/Documents/IR/Project2/postingslist.txt','w') #write to file
#path_of_input_queries = open('C:/Users/Astrid/Documents/IR/Project2/queries.txt','r')

path_of_output_result = open(output1,'w') #write to file
path_of_input_queries = open(queries1,'r')

line1 = path_of_input_queries.readline()

while line1:
    line=line1
    word_list=[]
    array_results_and=[]
    array_test_or=[]
    array_results_or=[]
    array_test_and=[]
    array_results_and_final=[]
    array_results_and_final1=[]
    tfidf_and=[]
    tfidf_or=[]
    count_or=0
    count_and=0
    for word in line.split():
        word_list.append(word)
    #print(word_list)
    len_wordlist=len(word_list)
    for j in word_list:
        #print(j)
        
        for k,v in new_dict.items():
            if(k==j):
                #print(k)
                path_of_output_result.writelines('GetPostings')
                path_of_output_result.writelines('\n')
                path_of_output_result.writelines(k)
                path_of_output_result.writelines('\n')
                path_of_output_result.writelines('Postings list: ')
                for f1 in range(0,len(v)):
                    if(f1==len(v)-1):
                        path_of_output_result.writelines(v[f1]) 
                    else:
                        path_of_output_result.writelines(v[f1]+' ') 
                if(len(array_test_and)==0):
                    for f2 in v:
                        array_test_and.append(f2)
                        count_and=count_and+1
                elif(len(array_test_and)!=0):
                    for f3 in v:
                        if(f3 in array_test_and):
                            array_results_and.append(f3)
                            count_and=count_and+1
                        else:
                            array_test_and.append(f3)
                            count_and=count_and+1
                            
                if(len(array_test_or)==0):
                    for f2 in v:
                        array_test_or.append(f2)
                        count_or=count_or+1   
                elif(len(array_test_or)!=0):
                    for f3 in v:
                        if(f3 in array_test_or):
                            array_results_or.append(f3)
                            count_or=count_or+1  
                        else:
                            array_test_or.append(f3) 
                            count_or=count_or+1        
                path_of_output_result.writelines('\n')
                
    #array_test_and.sort()         
    #(array_results_and_final) 
    array_results_and.sort()
    #set(array_results_and)
    #print(array_results_and)
    """
    if(len(word_list)>2):
        array_results_and_final= ([item for item, count in collections.Counter(array_results_and).items() if count > 1])
    else:
        array_results_and_final=array_results_and 
    """  
    if(len(word_list)>2):
        for i in range(len(array_results_and)): 
            k = i + 1
            for j in range(k, len(array_results_and)): 
                if array_results_and[i] == array_results_and[j] and array_results_and[i] not in array_results_and_final: 
                    array_results_and_final.append(array_results_and[i]) 
    else:
        array_results_and_final=array_results_and
    #print(array_results_and_final)    
    """
    for i in array_results_and:
        if(i not in array_results_and_final):
            array_results_and_final.append(i)
            """
    array_results_and_final.sort()
    #print(array_results_and_final)        
    array_test_or.sort()           
    path_of_output_result.write('DaatAnd') 
    path_of_output_result.writelines('\n')       
    for g in range(0,len(word_list)):  
        if(g==len(word_list)-1):
            path_of_output_result.writelines(word_list[g])
        else:  
            path_of_output_result.writelines(word_list[g]+' ')
        
        #print(g)          
        
    path_of_output_result.writelines('\n') 
    path_of_output_result.write('Results: ')        
    if(len(array_results_and_final)==0):
         
        path_of_output_result.writelines('empty') 
        path_of_output_result.writelines('\n')
    else:
        for u in range(0,len(array_results_and_final)):
            if(u==len(array_results_and_final)-1):
                path_of_output_result.writelines(array_results_and_final[u])
            else:    
                path_of_output_result.writelines(array_results_and_final[u]+' ')
                
            
        path_of_output_result.writelines('\n') 
      
    path_of_output_result.write('Number of documents in results: '+str(len(array_results_and_final)))    
    path_of_output_result.writelines('\n')  
    path_of_output_result.writelines('Number of comparisons: '+str(count_and)) 
    path_of_output_result.writelines('\n')     
    path_of_output_result.writelines('TF-IDF')
    path_of_output_result.writelines('\n')  
    path_of_output_result.writelines('Results: ') 
    if(len(array_results_and_final)==0):
         
        path_of_output_result.writelines('empty') 
    
    else:
        if(len(array_results_and_final)==1):
            for u in range(0,len(array_results_and_final)):
                if(u==len(array_results_and_final)-1):
                    path_of_output_result.writelines(array_results_and_final[u])
                else:
                    path_of_output_result.writelines(array_results_and_final[u]+' ')
                    
                
        else:       
            for g in array_results_and_final:
                path_of_output_result.writelines(g+' ')
    path_of_output_result.writelines('\n')  
        
    path_of_output_result.write('DaatOr') 
    path_of_output_result.writelines('\n') 
    for g in range(0,len(word_list)):  
        if(g==len(word_list)-1):
            path_of_output_result.writelines(word_list[g])
        else:
            path_of_output_result.writelines(word_list[g]+' ')
        #print(g)          
        
    path_of_output_result.writelines('\n')       
    path_of_output_result.write('Results: ')        
    if(len(array_test_or)==0):
        path_of_output_result.write('empty')  
        path_of_output_result.writelines('\n') 
        
    else:
        for u in range(0,len(array_test_or)):
            if(u==len(array_test_or)-1):
                path_of_output_result.writelines(array_test_or[u])
            else:    
                path_of_output_result.writelines(array_test_or[u]+' ')
        path_of_output_result.writelines('\n') 
      
    path_of_output_result.write('Number of documents in results: '+str(len(array_test_or)))    
    path_of_output_result.writelines('\n')  
    path_of_output_result.writelines('Number of comparisons: '+str(count_or)) 
    path_of_output_result.writelines('\n')   
    path_of_output_result.writelines('TF-IDF')
    path_of_output_result.writelines('\n')  
    path_of_output_result.writelines('Results: ') 
    if(len(array_test_or)==0):
        path_of_output_result.write('empty')  
    else:
        for u in range(0,len(array_test_or)):
            if(u==len(array_test_or)-1):
                path_of_output_result.writelines(array_test_or[u])
            else:    
                path_of_output_result.writelines(array_test_or[u]+' ')
        path_of_output_result.writelines('\n')  
    path_of_output_result.writelines('\n')   
        
    # use realine() to read next line
    line1 = path_of_input_queries.readline()
path_of_input_queries.close()
path_of_output_result.close()
path_of_input_corpus.close()