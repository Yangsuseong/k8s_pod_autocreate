import os
import subprocess as sp
import time
import fileinput
import sys
import pickle
import argparse


#--------------------------------
# Option help

default_image = "nvidia/cuda:11.4.1-base-ubuntu20.04"

parser = argparse.ArgumentParser(description='MW OST Tool')
parser.add_argument('-c', '--command', type=str, dest='command', required=True, default=False, help='Run command')
#parser.add_argument('-c', '--command', type=str, dest='command', default="cd /home/$namespace  && tail -f /dev/zero", help='Run command')
parser.add_argument('-n', '--name', type=str, dest='job_name', default=False, help='Select job name')
parser.add_argument('-g', '--gpus', type=str, dest='gpu_count', default='1', help='Number of GPU usage. Default=0')
parser.add_argument('-i', '--image', type=str, dest='image_name', default=default_image, help='Select image')
args = parser.parse_args()

#--------------------------------


def job_name_check():
    global user_name
    user_name = str(os.popen("whoami").read())
    user_name = user_name.rstrip('\n')
    #print(user_name)

    os.system(str("kubectl get pod | grep -i / | awk '{print $1}' > ./k8s_pod_name"))

    f = open("./k8s_pod_name", "rt", encoding="utf-8")
    name = f.readlines()
    f.close()
    os.system("rm ./k8s_pod_name")
    
    name = "".join(name).split("\n")

    var = 0
    var_list = []

    for i in range(len(name)):
        #print(i)
        var = "".join(name[i]).split(" ")
        #print(var)
        var_list.append(var)

    var_list = var_list[:-1]

    #print(var_list)

    name_list = []
    for i in range(len(var_list)):
        temp=[]
        temp = ' '.join(var_list[i]).split()
        #print(temp[-1])
        name_list.append(temp[-1])

    #print(name_list)

    idx = 0
    container_name = ""
    #for i in range(len(name_list)):
    while True:
        idx_1 = 0
        idx_2 = 0
        temp = user_name + "-autocreate-" + str(idx)
        idx += 1
        #print(len(name_list))
        if(len(name_list) == 0):
            container_name = temp
            break
        for j in name_list:
            if(str(temp) == j):
                #print("name_list :", j, "temp : ", temp)
                continue
            else:
                idx_1 += 1

            if(idx_1 == len(name_list)):
                idx_2 += 1
                container_name = temp
                #print(container_name)
        if (idx_2 == 1):
            break
    return container_name

def user_uid():
    global user_uid
    user_uid = str(os.popen("id -u").read())
    user_uid = user_uid.rstrip('\n')
    #print(user_uid)
    return user_uid



# Logo & Copyright
###################################################################

def logo_copyright_print():
    for i in range(3):
        print(" ")
    print("###########################################################################")
    print("#                                                                         #")
    print("#        #########      ##########     ####                ####           #")
    print("#        ##########    ###########     ####                ####           #")
    print("#        ####   ####  ####    ####     ####                ####           #")
    print("#        ####    ########     ####     ####      ####      ####           #")
    print("#        ####      ####       ####     ####    ########    ####           #")
    print("#        ####                 ####     ####   ####  ####   ####           #")
    print("#        ####                 ####     ##########    ##########           #")
    print("#        ####                 ####     #########      #########           #")
    print("#                                                                  OST    #")
    print("###########################################################################")
    for i in range(3):
        print(" ")

    print("****************************************")
    print("-Miruware-")
    print("Made by Suseong Yang")
    print("Email : tntjd5596@miruware.com, mw@miruware.com")
    print("****************************************")
    for i in range(3):
        print(" ")






#args setting
logo_copyright_print()
job_name = job_name_check()
uid = user_uid()
user = user_name
print("command : " + str(args.command))
if args.__dict__['job_name']:
    print("job_name : " + str(args.job_name))
else:
    print("job_name : " + job_name)
print("gpus : " + str(args.gpu_count))
print("image : " + str(args.image_name))
print("user : " + str(user))
print("uid : " + str(uid))
print("------------------------")




#run
if args.__dict__['job_name']:
    if args.__dict__['gpu_count']:
        if args.__dict__['image_name']:
            os.system("bash ./gpu-demo-python.yaml " + user + " " + uid + " " + args.job_name + " '" + args.command + "' " + args.gpu_count + " " + args.image_name)
            #print("bash ./gpu-demo-python.yaml " + user + " " + uid + " " + args.job_name + " '" + args.command + "' " + args.gpu_count + " " + args.image_name)
        else:
            os.system("bash ./gpu-demo-python.yaml " + user + " " + uid + " " + args.job_name + " '" + args.command + "' " + args.gpu_count + " " + args.image_name)
            #print("bash ./gpu-demo-python.yaml " + user + " " + uid + " " + args.job_name + " '" + args.command + "' " + args.gpu_count + " " + args.image_name)
    else:
        os.system("bash ./gpu-demo-python.yaml " + user + " " + uid + " " + args.job_name + " '" + args.command + "' " + args.gpu_count + " " + args.image_name)
        #print("bash ./gpu-demo-python.yaml " + user + " " + uid + " " + args.job_name + " '" + args.command + "' " + args.gpu_count + " " + args.image_name)
else:
    if args.__dict__['gpu_count']:
        if args.__dict__['image_name']:
            os.system("bash ./gpu-demo-python.yaml " + user + " " + uid + " " + job_name + " '" + args.command + "' " + args.gpu_count + " " + args.image_name)
            #print("bash ./gpu-demo-python.yaml " + user + " " + uid + " " + job_name + " '" + args.command + "' " + args.gpu_count + " " + args.image_name)
        else:
            os.system("bash ./gpu-demo-python.yaml " + user + " " + uid + " " + job_name + " '" + args.command + "' " + args.gpu_count + " " + args.image_name)
            #print("bash ./gpu-demo-python.yaml " + user + " " + uid + " " + job_name + " '" + args.command + "' " + args.gpu_count + " " + args.image_name)
    else:
        os.system("bash ./gpu-demo-python.yaml " + user + " " + uid + " " + job_name + " '" + args.command + "' " + args.gpu_count + " " + args.image_name)
        #print("bash ./gpu-demo-python.yaml " + user + " " + uid + " " + job_name + " '" + args.command + "' " + args.gpu_count + " " + args.image_name)

