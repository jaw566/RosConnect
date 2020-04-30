#!/usr/bin/env python3

# Description: Loop through all files in Scripts directory and set the password (to be used in ssh call)
#              to the password argument given by the caller of this function

import os
import sys

def main():

    if len(sys.argv) != 4:
        print("Incorrect number of arguments given")
        print("Please run as ./mk_hostname_and_password [vehicle_id]  [vehicle_hostname] [password]")
        print("e.g., ./mk_hostname_andpassword 10.18.92.120 nvidia password")
        return -1
    
    host = str(sys.argv[1])
    hostname = str(sys.argv[2])
    password = str(sys.argv[3])

    HOME  = os.environ['HOME']

    files = os.listdir(HOME+'/RosConnect/Scripts') 

    for f in files:
        with open(HOME+'/RosConnect/Scripts/'+f,'r') as file:
            data = file.readlines()

        line_ctr=0
        for line in data:
            line_split = line.split()
            if line_split != [] and line_split[0] == 'sshpass':
                if( str(line_split[3]) == "scp"):
                   new_split = line_split[9]
                   new_split = new_split.split(":")
                   new_value = new_split[0]
                   second = new_split[1]
                   loc = 9
                   host_value = new_value.split("@")
                   line_split = change_host(host_value, host, line_split, loc,hostname, second) 
                else:
                   other_split = line_split[5]
                   loc = 5
                   host_values = other_split.split("@")
                   line_split = change_host(host_values, host,line_split, loc,hostname, None)
                line_split[2] = "'"+password+"'"
                data[ line_ctr ] = " ".join( line_split )+"\n"
            line_ctr+=1

        with open(HOME+'/RosConnect/Scripts/'+f,'w') as file:
            file.writelines(data)


def change_host(line, host, line_split, loc, hostname, scp):
    host_name = hostname
    new_host = host_name + str("@") + host
    if scp is not None:
        new_host = new_host + ":" + scp
    line_split[loc] = new_host
    
    return line_split

if __name__ == "__main__":

    main()    
