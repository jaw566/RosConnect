#!/bin/bash


sshpass -p 'newpassword' ssh -T nvidia@10.18.92.160 "pkill ros"
