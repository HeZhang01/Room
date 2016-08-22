#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <errno.h>
#include <string.h>
#include <netinet/in.h>
#include <unistd.h>

#define MAXLINE  4096

int socket_create(){
    int sock_fd = socket(AF_INET,SOCK_STREAM,0);
    if(-1 == sock_fd){
        printf("socket create error!");
        return -1;
    }
    return sock_fd;
}

int socket_bind(){
    // int sock_bind = bind();
}


int main(){
    int sock_fd,newsock_fd;
    struct sockaddr_in servaddr;
    char buff[4096];
    int n;
    // create socket
    sock_fd = socket(AF_INET,SOCK_STREAM,0);
    if(sock_fd == -1){
        printf("socket create errer:%s (errno:%d)",strerror(errno),errno);
        exit(0);
    }

    // bind socket
    memset(&servaddr,0,sizeof(servaddr));
    servaddr.sin_family      = AF_INET;
    servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
    servaddr.sin_port        = htons(6666);
    if( -1 == bind( sock_fd,(struct sockaddr*) &servaddr,sizeof(servaddr) ) ){
        printf("socket bind errer:%s (errno:%d)",strerror(errno),errno);
        exit(0);
    }

    // listen socket
    if(-1 == listen(sock_fd,10)){
        printf("socket listen errer:%s (errno:%d)",strerror(errno),errno);
        exit(0);

    }
    
    // accept socket
    printf("======waiting for client's request======\n");
    while(1){
        if( -1 == (newsock_fd=accept(sock_fd,(struct sockaddr*) NULL,NULL)) ){
            printf("socket accept errer:%s (errno:%d)",strerror(errno),errno);
            continue;
        }
        n = recv(newsock_fd,buff,MAXLINE,0);
    	buff[n] = '\0';
        printf("recv msg from client: %s\n", buff);
        close(newsock_fd);
    }
    close(sock_fd);

    return 0;
}
