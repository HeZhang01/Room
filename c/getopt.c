#include <stdio.h>
#include <unistd.h>

int main(int argc,char **argv)
{
    char ch;
    while( (ch=getopt(argc,argv,"a:bc::d")) != -1 )
        switch(ch)
	{
	    case 'a':
	        printf("option a: %s\n",optarg);
		break;
	    case 'b':
		printf("params b: %s\n",optarg);
		break;
	    case 'c':
		printf("option c: %s\n",optarg);
		break;
	    case 'd':
		printf("params d: %s\n",optarg);
	    default:
	        printf("error option %c %c\n",optopt,ch);
	}	    

}
