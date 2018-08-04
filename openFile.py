import urllib2

fh = open("domainlist.txt","r")
          
List = fh.readlines()
list2 = []
statusCode=[] 
q=0
error =0
ecode = 0
          
length = len(List)

print("*** Total Subdomains = "+str(length)+" ***")


for index in range(length):
    
    #print("\nhttp://"+List[index])
    print("*** Processing *********")
         
    
    try:
      
        q =urllib2.urlopen("http://"+List[index]).
        statusCode.append(q)  
        list2.append(List[index])
        
         

    except urllib2.HTTPError as e:
         
         if(e.code==404):
             list2.append(List[index])
             statusCode.append(e.code)  
             ecode = ecode+1
         else:

              list2.append(List[index])
              statusCode.append(e.code)  
              ecode = ecode+1
              
                

    except urllib2.URLError as e:
            error =error+1
            statusCode.append(-1)
           
    
print("Total Non Reachable Error = "+ str(error))

print("Total Status code other than 200 = "+ str(ecode))

print("\n********** Final Accessible Websites **********")
lengths = len(list2)

print("\n********** Total Reachable Subdomains = "+str(lengths)+" **********\n")

for index in range(lengths):
    
    print(list2[index] + " --> "+ str(statusCode[index])+ "\n")
