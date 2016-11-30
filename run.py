###############################################
##     Bezel Online Judge                     #
##     Version 1.0                            #
##     Himanshu Dixit,Utkarsh Dixit           #
##     file - RUN.PY                          #
###############################################

import os,filecmp,io
import subprocess

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
        else if lang = 'javascript':
            extn = 'js'

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


def compiler(id,lang):

        if lang = 'c++ 5.1':
            filepath = dir+id+'.cpp'
            command = 'gcc -o '+filepath
        else if lang = 'c++ 14.1':
            filepath = dir+id+'.cpp'
            command = 'gcc -std=c++1y -o '+filepath
        else if lang = 'bash':
            filepath = dir+id+'.sh'
            command = 'sh '+filepath
        else if lang = 'java':
            filepath = dir+id+'.java'
            command = 'javac '+filepath
        else if lang = 'java7':
            filepath = dir+id+'.java'
            # New Environment Variable java7 must be created to use this
            command = 'java7 '+filepath
        else if lang = 'haskell':
            filepath = dir+id+'.hs'
            command = 'ghc '+filepath
        else if lang = 'pascalfpc':
            filepath = dir+id+'.pas'
            command = 'fpc '+filepath
        else if lang = 'pascalgpc':
            filepath = dir+id+'.pas'
            command = 'gpc '+filepath
        else if lang = 'perl':
            filepath = dir+id+'.pl'
            command = 'perl -c '+filepath
        else if lang = 'python2.7':
            filepath = dir+id+'.py'
            command = 'python -m py_compile '+filepath
        else if lang = 'python3.4':
            filepath = dir+id+'.py'
            command = 'python3 -m py_compile '+filepath
        else if lang = 'javascript':
            filepath = dir+id+'.js'
            #using rhino interpreter
            command = 'rhino '+filepath
        #This will compile the script
        shell_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        shell_process.wait()
        shell_return = shell_process.returncode



def run(code,language,source):
    print "Processing File Started"

def check(code,language,source):
    print "Processing File Started"

def terminate(id):
    print "Processing File Started"
