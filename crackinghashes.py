import hashlib
import timeit
import sys
from multiprocessing import Process, current_process
start_time = timeit.default_timer()

hash = sys.argv[1]
classification = sys.argv[2]
salt = sys.argv[3]

file = open('passwordlist.txt','r')
passwordlist = file.read().splitlines()

#Set count for program to 0

limit = len(passwordlist)

def crackHash(inputHash,limit):
    count=1;
    for x in range(0,limit):
        test = hashlib.sha1(passwordlist[x]).hexdigest()
        if inputHash == test:
            elapsed = timeit.default_timer() - start_time
            print "This is the hash for the password " + passwordlist[x]
            print "It only took " + str(count) + " tries!"
            print "It took" + str(elapsed) + " seconds to complete!"
            return passwordlist[x]
            break
        else:
            count+=1

def solveSaltHash(saltHash,limit,finalHash):
    count=1;
    #Time the program
    for x in range(0,limit):
        test = hashlib.sha1(passwordlist[x]).hexdigest()
        if saltHash == test:
            print "It took " + str(count) + " tries to find the salted value " + passwordlist[x]
            saltString = passwordlist[x]
        else:
            count+=1
    countpass = count
    saltvalue = saltString
    solveSaltHash2(saltvalue,finalHash,countpass)            

def solveSaltHash2(salt,finalHash,counter): 
    count=counter
    for x in range(0,limit):
        password = salt+passwordlist[x]
        test = hashlib.sha1(salt+passwordlist[x]).hexdigest()
        if finalHash == test:
            elapsed = timeit.default_timer() - start_time
            print "This is the hash for the password " + password
            print "It took " + str(count) + " tries in total to solve the salt and hash!"
            print "It took " + str(elapsed) + " seconds to complete!"
        else:
             count+=1


def complexHash(inputHash,limit,password):
    #Using the "os" id to get the process id associated with this function call, assigned by the OS
    for x in range(0,limit):
        passwordValue1 = password+" "+passwordlist[x]
        print(passwordValue1)
        test = hashlib.sha1(passwordValue1).hexdigest()
        if inputHash == test:
            elapsed = timeit.default_timer() - start_time
            print "This is the hash for the password" + passwordValue1
            print "It took " + str(count) + " tries in total to solve the complex hash!"                    
            print elapsed
            break
        else:
            count+=1




if(classification == 'hashonly'):
    crackHash(hash,limit)
elif(classification == 'salted'):
    solveSaltHash(salt,limit,hash)

elif(classification == 'complex'):
    if __name__ == "__main__":
        processes = []
        for x in range(0,1):
            process = Process(target=complexHash, args=(hash,limit,passwordlist[x]))
            processes.append(process)

            #Processes are spawned by cerating a process object then calling its start method
            process.start()
        

