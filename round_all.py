#conding=utf8  
import os 

g = os.walk(r"./pushup")  

for path,dir_list,file_list in g:  
    for file_name in file_list:  
        file_paths=os.path.join(path, file_name)
        file_paths=file_paths.replace("\\","/")
        print(file_paths)