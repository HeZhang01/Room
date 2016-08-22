#include <unistd.h>
#include <stdlib.h>

#define MAXLINE 10

int main()
{
	int n;
	char buf[MAXLINE];
	n=read(STDIN_FILENO,buf,MAXLINE);
	write(STDOUT_FILENO,buf,n);

	return 0;
}
