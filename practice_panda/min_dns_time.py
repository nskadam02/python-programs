
# Online Python - IDE, Editor, Compiler, Interpreter

#cache_size,cache_time,server_time ,urls
#3,3,2
def find_min(cache_size,cache_time,server_time,urls):
    cache=[]
    min_time=[]
    for i in range(1,len(urls)+1):
        j=i-1
        if(len(cache)!=cache_size):
            if(urls[j] not in cache):
                min_time.append(server_time)
            else:
                min_time.append(cache_time)
            cache.append(urls[j])
        else:
            if(urls[j] in cache):
                min_time.append(cache_time)
            else:
                min_time.append(server_time)
            cache.pop(0)
            cache.append(urls[j])
    return min_time
    
    
                
        



result = find_min(2,2,3,["a","b","a","b","d"])
print(result)