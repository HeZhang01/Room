#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <errno.h>
#include <string.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>

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


int main(int argc,char **argv){
    int sock_fd;
    struct sockaddr_in servaddr;
    char buff[4096];
    int n;

    if( argc != 2){
        printf("usage: ./client <ipaddress>\n");
        exit(0);
    }

    // create socket
    sock_fd = socket(AF_INET,SOCK_STREAM,0);
    if(sock_fd == -1){
        printf("socket create errer:%s (errno:%d)",strerror(errno),errno);
        exit(0);
    }

    //  format socketaddr
    memset(&servaddr,0,sizeof(servaddr));
    servaddr.sin_family      = AF_INET;
    servaddr.sin_port        = htons(6666);
    if( inet_pton(AF_INET,argv[1],&servaddr.sin_addr) < 0 ){
        printf("inet_pton error for %s\n",argv[1]);
        exit(0);
    }

    // connect socket
    if( connect(sock_fd,(struct sockaddr*)&servaddr,sizeof(servaddr)) < 0 ){
        printf("socket connnect errer:%s (errno:%d)",strerror(errno),errno);
        exit(0);

    }
    
    // send msg
    printf("====send msg to server=====: \n");
    fgets(buff, 4096, stdin);
    if( send(sock_fd, buff, strlen(buff), 0) < 0)
    {
    printf("send msg error: %s(errno: %d)\n", strerror(errno), errno);
    exit(0);
    }

    printf("send msg successful! \n");
    close(sock_fd);
    exit(0);

    return 0;
}
