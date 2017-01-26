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

dir = 'temp/code_location/'

#Create Function To Get Data

def create(id,code,lang,source):
        if lang == 'c':
            extn = '.c'
        elif lang == 'c++ 5.1':
            extn = '.cpp'
        elif lang == 'c++ 14.1':
            extn = '.cpp'
        elif lang == 'bash':
            extn = '.sh'
        elif lang == 'java':
            extn = '.java'
        elif lang == 'java7':
            extn = '.java'
        elif lang == 'haskell':
            extn == '.hs'
        elif lang == 'pascalfpc':
            extn = '.pas'
        elif lang == 'pascalgpc':
            extn = '.pas'
        elif lang == 'perl':
            extn = '.pl'
        elif lang == 'python2.7':
            extn = '.py'
        elif lang == 'python3.4':
            extn = '.py'
        elif lang == 'javascript':
            extn = '.js'

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


def compile(id,lang):
        print "Compiling File"
        if lang == 'c':
            filepath = dir+id+'.c'
            command = 'gcc '+filepath+' -o '+dir+id
        elif lang == 'c++ 5.1':
            filepath = dir+id+'.cpp'
            command = 'gcc '+filepath+' -o '+dir+id
        elif lang == 'c++ 14.1':
            filepath = dir+id+'.cpp'
            command = 'gcc -std=c++1y '+filepath+' -o '+dir+id
        elif lang == 'bash':
            filepath = dir+id+'.sh'
            command = ''
        elif lang == 'java':
            filepath = dir+id+'.java'
            command = 'javac '+filepath
        elif lang == 'java7':
            filepath = dir+id+'.java'
            # New Environment Variable java7 must be created to use this
            command = 'java7 '+filepath
        elif lang == 'haskell':
            filepath = dir+id+'.hs'
            command = 'ghc '+filepath
        elif lang == 'pascalfpc':
            filepath = dir+id+'.pas'
            command = 'fpc '+filepath
        elif lang == 'pascalgpc':
            filepath = dir+id+'.pas'
            command = 'gpc '+filepath
        elif lang == 'perl':
            filepath = dir+id+'.pl'
            command = 'perl -c '+filepath
        elif lang == 'python2.7':
            filepath = dir+id+'.py'
            command = 'python -m py_compile '+filepath
        elif lang == 'python3.4':
            filepath = dir+id+'.py'
            command = 'python3 -m py_compile '+filepath
        elif lang == 'javascript':
            filepath = dir+id+'.js'
            #using rhino interpreter
            #command = 'rhino '+filepath
        #This will compile the script
        shell_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        shell_process.wait()
        shell_return = shell_process.returncode
        if(shell_return > 10):
            #Error
            return 1001
        else:
            #File Has Been Compiled
         return 2001

def run(id,lang,timeout):
    filepath = dir+id
    if lang == 'java':
     cmd = 'java '+filepath
    elif lang == 'java7':
     cmd = 'java7 '+filepath
    elif lang=='c++ 5.1' or lang=='c++ 14.1' or lang=='c':
     cmd = './'+id
     os.system("cd "+dir)
    elif lang=='python2.7':
     cmd = 'python '+filepath
    elif lang=='python3.4':
     cmd = 'python3 '+filepath
    elif lang=='javascript':
     cmd = 'rhino '+filepath
    elif lang=='bash':
     cmd = 'sh '+filepath
    elif lang=='pel':
     cmd = 'pel '+filepath
    elif lang=='gpc':
     cmd = 'sh '+filepath
    elif lang=='fpc':
     cmd = 'fpc '+filepath
    elif lang=='haskell':
     cmd = 'ghc '+filepath
    input = '1'

    os.chdir("/home/osboxes/Desktop/Bezel/temp/code_location/")
    #os.system("touch "+dir+id+".out")
    r = os.system("timeout "+timeout+" "+cmd+" > "+id+".out")
    #print r
    #print "timeout "+timeout+" "+cmd+" &> "+id+".out"
    print "Running File"

def check(id):
    print "Checking File"

    if(filecmp.cmp(id+'.in', id+'.out',shallow=False)):
        return 2003
    else:
        return 1006

def terminate(id):
    print 'Terminating'
    #command = 'rm -f '+dir+id+'*'
    #shell_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    #shell_process.wait()
    #shell_return = shell_process.returncode
    #if(shell_return):
        #File Not Deleted
        #return 3001
    #else:
        #All Files Deleted
        #return 1000

#main calling

id='35'
lang = 'c'
source = 5000 #5 MB, to be customized
code = """#include<stdio.h>
int main()
{
    printf("1"); return 0;
}
"""
timeout = '1' #secs
create = create(id,code,lang,source)

if(create==2000):
    #file succesfullt create
    compile = compile(id,lang)
    if(compile==2001):
        print 'File has been compiled'
        run = run(id,lang,timeout)
        if(run==1004 or run==1007):
            print("Runtime Error")
            terminate(id)
        else:
            check = check(id)
            if(check == 2003):
             print 'Correct Answer'
            else:
             print 'Wrong Answer'

            terminate(id)
    else:
        print 'Compilation Error'
        terminate(id)
elif(create==1005):
    print 'Source Limit Exceeded'
else:
    print 'Some Error ocurred'
