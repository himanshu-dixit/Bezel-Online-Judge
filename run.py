###############################################
##     Bezel Online Judge                     #
##     Version 1.0                            #
##     Himanshu Dixit,Utkarsh Dixit           #
##     file - RUN.PY                          #
###############################################

import os,filecmp,io
import subprocess

#Response Codes To Be Used Further

response = {1000:'Some Error Occured',1001:'Compilation Error',1002:'Runtime Error',1003:'Memory Limit Exceeded',1004:'Time Limit Exceeded',1005:'Source Limit Exceeded',1006:'Wrong Answer',1007:'Unknown Error',2000:'File Created',2001:'File Compiled',2003:'Correct Answer'}
#Path to temporaray location

dir = '/temp/code_location'

#Create Function To Get Data

def create(id,code,lang,source):
        if lang = 'c':
            extn = 'c'
        else if lang = 'c++ 5.1':
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

        if lang = 'c':
            filepath = dir+id+'.c'
            command = 'gcc'+filepath+' -o '+dir+id
        else if lang = 'c++ 5.1':
            filepath = dir+id+'.cpp'
            command = 'gcc'+filepath+' -o '+dir+id
        else if lang = 'c++ 14.1':
            filepath = dir+id+'.cpp'
            command = 'gcc -std=c++1y '+filepath+' -o '+dir+id
        else if lang = 'bash':
            filepath = dir+id+'.sh'
            command = ''
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
        if(len(shell_return) > 10):
            #Error
            return 1001
        else:
            #File Has Been Compiled
            return 2001




def run(id,lang,timeout):
    if lang == 'java':
     cmd = 'java '+filepath
    else if lang == 'java7':
     cmd = 'java7 '+filepath
    elif lang=='c++ 5.1' or lang=='c++ 14.1' or lang=='c':
     cmd = './'+filepath
    elif lang=='python2.7':
     cmd = 'python '+filepath
    elif lang=='python3.4':
     cmd = 'python3 '+filepath
    r = os.system('timeout '+timeout+' '+cmd+' < '+input+' > out.txt')
    print "Running File"

def check(id):
    if(filecmp.cmp(id+'.in', id+'.out')):
        return 2003
    else:
        return 1006
    print "Processing File Started"

def terminate(id):
    command = 'rm -f '+dir+id+'*'
    shell_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    shell_process.wait()
    shell_return = shell_process.returncode
    if(shell_return):
        #File Not Deleted
    else:
        #All Files Deleted
