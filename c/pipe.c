#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>


#define MAXLINE 80


/**
* 限制：
* 1.单向通讯
* 2.需要通过fork来传递文件描述符
*/


int main(){
    pid_t pid;
    int fd[2];
    char buf[MAXLINE];
    int n;

    if( pipe(fd) < 0 ){
        perror("pipe error");exit(1);
    }

    if( (pid = fork()) < 0){
        perror("fork failed");exit(1);
    }

   if(pid > 0){
        close(fd[0]);
        write(fd[1],"Hello world!\n",13);
        wait(NULL);
   }else{
       close(fd[1]);
       n = read(fd[0],buf,MAXLINE);
       write(STDOUT_FILENO,buf,n);
   }

   return 0;

}
