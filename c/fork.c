#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

int main(){
    pid_t pid;
    int n;
    char *message;
    pid = fork();
    if(pid < 0){
        perror("fork failed");
        exit(1);
    }else{
        if(pid == 0){
            message = "This is child\n";
	    n = 6;
        }else{
	    message = "This is parent\n";
	    n = 3;
	}
    }
    
    while(n > 0){
        printf("%s",message);
        n--;
        sleep(1);
    }
    
    return 0;
}
