#ALGORITHMS FOR FILE UPDATES (PYTHON)

allowed_file = "data/allowed_list.txt"          #Currently allowed IP
to_remove_file = "data/to_remove_list.txt"      #To be removed IP

#Main IP List
with open(allowed_file, "r") as file:           #Open the file that contains allowed list.
    allowed_ip = file.read()                    #Read the file contents

allowed_ip = allowed_ip.split()                 #Convert strings into a list

with open(to_remove_file, "r") as file:         #Open the file that contains to be removed list.
    remove_list = file.read()                   #Read the file contents

remove_list = remove_list.split()               #Convert strings into a list

#Iterate through lists to check
for ip in remove_list:
    if ip in allowed_ip:
        allowed_ip.remove(ip)

allowed_ip = "\n".join(allowed_ip)

updated_file = "data/updated_list.txt"    #Create file to put updated list
with open(updated_file, "w") as file:
    file.write(allowed_ip)

with open(updated_file, "r") as file:
    read_upd = file.read()

print(read_upd)


