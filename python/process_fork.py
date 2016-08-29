import os

"""
fork函数是POSIX的一种实现，不适用于Windows

"""
print('Process ({}) start...'.format( os.getpid()) )
pid = os.fork()
if pid == 0:
    print('I am child process ({}) ,my parent is ({})'.format( os.getpid(), os.getppid() ))
else:
    print('I ({}) just create a child process ({})'.format( os.getpid(), pid ))
