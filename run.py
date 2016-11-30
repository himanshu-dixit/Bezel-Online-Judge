###############################################
##     Bezel Online Judge                     #
##     Version 1.0                            #
##     Himanshu Dixit,Utkarsh Dixit           #
##     file - RUN.PY                          #
###############################################

import os,filecmp,io

#Response Codes To Be Used Further

response = {1000:'Some Error Occured',1001:'Compilation Error',1002:'Runtime Error',1003:'Memory Limit Exceeded',1004:'Time Limit Exceeded',1005:'Source Limit Exceeded',1006:'Wrong Answer',1007:'Unknown Error',2000:'File Created'}
#Path to temporaray location

dir = '/temp/code_location'

#Create Function To Get Data

def create(id,code,lang,source):
        if lang = 'c++ 5.1':
            extn = 'cpp'
        else if lang = 'c++ 14.1':
            extn = 'cpp'
        else if lang = 'bash':
            extn = 'sh'
        else if lang = 'java':
            extn = 'java'
        else if lang = 'java7':
            extn = 'java'
        else if lang = 'haskell':
            extn = 'hs'
        else if lang = 'pascalfpc':
            extn = 'pas'
        else if lang = 'pascalgpc':
            extn = 'pas'
        else if lang = 'perl':
            extn = 'pl'
        else if lang = 'python2.7':
            extn = 'py'
        else if lang = 'python3.4':
            extn = 'py'
        else if lang = 'ruby':
            extn = 'rb'
        else if lang = 'javascript':
            extn = 'js'
        else if lang = 'brainfuck':
            extn = 'bf'

        filepath = dir+id+extn

        if(os.path.isfile(filepath)):
            os.remove(filepath)

        #Create File
        with io.FileIO(filepath, "w") as file:
            file.write(code)

        #Source Limit Exceeded
        if(os.path.getsize(filepath) > source):
            terminate(id)
            return 1005

        if(os.path.isfile(filepath)):
            return 2000
        else:
            return 1000


def compiler(code,language,source):
        if lang = 'c++ 5.1':
            extn = 'cpp'
        else if lang = 'c++ 14.1':
            extn = 'cpp'
        else if lang = 'bash':
            extn = 'sh'
        else if lang = 'java':
            extn = 'java'
        else if lang = 'java7':
            extn = 'java'
        else if lang = 'haskell':
            extn = 'hs'
        else if lang = 'pascalfpc':
            extn = 'pas'
        else if lang = 'pascalgpc':
            extn = 'pas'
        else if lang = 'perl':
            extn = 'pl'
        else if lang = 'python2.7':
            extn = 'py'
        else if lang = 'python3.4':
            extn = 'py'
        else if lang = 'ruby':
            extn = 'rb'
        else if lang = 'javascript':
            extn = 'js'
        else if lang = 'brainfuck':
            extn = 'bf'



def run(code,language,source):
    print "Processing File Started"

def check(code,language,source):
    print "Processing File Started"

def terminate(id):
    print "Processing File Started"
