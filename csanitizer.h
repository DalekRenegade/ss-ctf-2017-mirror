#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int checkIfBlockIsByteCode(char *ptr)
{
	if((ptr[0] == '\\' || ptr[0] == '0') && ptr[1] == 'x' && (ptr[2] >= '0' && ptr[2] <= '9') && (ptr[3] >= '0' && ptr[3] <= '9'))
		return 1;
	return 0;
}

char* sanitizeShellCode(char *arg, int shouldFreeArg)
{
	int len = strlen(arg);
	char *newarg = (char*)calloc(len+1, sizeof(char));
	memset(newarg, 0, len+1);
	int i=0, j=0;
	while(i<len)
	{
		if(checkIfBlockIsByteCode(&(arg[i])) == 1)
			i+=4;
		else
			newarg[j++] = arg[i++];
	}
	if(shouldFreeArg == 1)
		free(arg);
	return newarg;
}

char* sanitizePathVulnerability(char *arg, int shouldFreeArg)
{
	int len = strlen(arg);
	char *newarg = (char*)calloc(len+1, sizeof(char));
	memset(newarg, 0, len+1);
	int i=0, j=0;
	while(i<len)
	{
		if((arg[i] == '.' && arg[i+1] == '.') || (arg[i] == '%' && arg[i+1] == 'n'))
			i+=2;
		else if(arg[i] == '%' && arg[i+1] == 'h' && arg[i+2] == 'h' && arg[i+3] == 'n')
			i+=4;
		else
			newarg[j++] = arg[i++];
	}
	if(newarg[0] == '~')
		newarg[0] = '/';
	if(shouldFreeArg == 1)
		free(arg);
	return newarg;
}

char* sanitizeCommandInjection(char *arg, int shouldFreeArg)
{
	int len = 0, flag = 0, maxColumns = 50;
	while(len<strlen(arg))
	{
		if(arg[len] == ';' || arg[len] == '&' || arg[len] == '|')
			break;
		len++;
	}
	char *newarg = (char*)calloc(len + 1, sizeof(char));
	memset(newarg, 0, len + 1);
	arg[len] = '\0';
	if(len < strlen(arg))
		free(&(arg[len+1]));
	FILE *fp = fopen("/var/restricted_cmd.txt", "r");
	if (fp > 0)
	{
		char command[maxColumns];
		while (fgets(command, sizeof(command), fp))
		{
			command[strlen(command) - 1] = '\0';
			char *p = strstr(arg, command);
			if(p == arg || (p != NULL && (p[-1] == ' ' || p[-1] == '/')))
			{
				flag = 1;
				break;
			}
		}
		if(flag == 0)
			strncpy(newarg, arg, len);
	}
	fclose(fp);
	if(shouldFreeArg == 1)
		free(arg);
	return newarg;
}

char** init(int argc, char *argv[])
{
	int len = strlen(argv[0]);
	char **newargv = (char**)calloc(argc, sizeof(char*));
	newargv[0] = (char*)calloc(len + 1, sizeof(char));
	memset(newargv[0], 0, len+1);
	strncpy(newargv[0], argv[0], len);
	for(int i=1;i<argc;i++)
	{
		len = strlen(argv[i]);
		char *newarg = sanitizeShellCode(argv[i], 0);
		newargv[i] = sanitizePathVulnerability(newarg, 1);
	}
	return newargv;
}

char** init2(int argc, char *argv[])
{
	int len = strlen(argv[0]);
	char **newargv = (char**)calloc(argc, sizeof(char*));
	newargv[0] = (char*)calloc(len + 1, sizeof(char));
	memset(newargv[0], 0, len+1);
	strncpy(newargv[0], argv[0], len);
	for(int i=1;i<argc;i++)
	{
		len = strlen(argv[i]);
		char *newarg = sanitizeShellCode(argv[i], 0);
		newarg = sanitizePathVulnerability(newarg, 1);
		newargv[i] = sanitizeCommandInjection(newarg, 1);
	}
	return newargv;
}

void freeMemory(int argc, char **argv)
{
	for(int i=0;i<argc;i++)
		free(argv[i]);
	free(argv);
}
