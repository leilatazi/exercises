
#%% The new line character is : \n
# all actions on the keyboard are associated to a character
# the int function ignores white spaces

def print_file_uppercase(file_path):
    
    try:
        file = open(file_path)
    
        for line in file:
            if line.isupper():
                print((line).strip())
                
    except Exception:
        print("file doesn´t exist")

print_file_uppercase("data.txt")

#%%
# parsing is to convert example a text into a list of rows
# csv means comma separated values

def parse_csv(filename, seperator=","):
    
    file = open(filename)
    csv = []
    
    for line in file:
         csv.append(line.strip().split(seperator))
            
    return csv   

csv = parse_csv("data.csv")

#%% 
#

def copy_file(origin, destination):
    
    try:
        origin_file = open(origin)
        destination_file = open(destination, "w")
        
#        if len((origin_file.read())) == 0 
        
        for line in origin_file:
            destination_file.write(line)
    
    except Exception:
        print("something went wrong")

    
    
    