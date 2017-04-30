#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int checkIfBlockIsByteCode(char *ptr)
{
	if((ptr[0] == '\\' || ptr[0] == '0') && ptr[1] == 'x' && (ptr[2] >= '0' && ptr[2] <= '9') && (ptr[3] >= '0' && ptr[3] <= '9'))
		return 1;
	return 0;
}

char* sanitizeShellCode(char *arg)
{
	int len = strlen(arg);
	char *newarg = (char*)calloc(len+1, sizeof(char));
	memset(newarg, 0, len+1);
	int i=0, j=0;
	while(i<len)
	{
		if(checkIfBlockIsByteCode(&(arg[i])))
			i+=4;
		else
			newarg[j++] = arg[i++];
	}
	return newarg;
}

char* sanitizePathVulnerability(char *arg)
{
	int len = strlen(arg);
	char *newarg = (char*)calloc(len+1, sizeof(char));
	memset(newarg, 0, len+1);
	int i=0, j=0;
	while(i<len)
	{
		if(arg[i] == '.' && arg[i+1] == '.')
			i+=2;
		else
			newarg[j++] = arg[i++];
	}
	if(newarg[0] == '~')
		newarg[0] = '/';
	free(arg);
	return newarg;
}

char* sanitizeCommandInjection(char *arg)
{
	int len=0, flag=0, maxColumns = 20;
	
	while(arg[len] != ';' || arg[len] != '&' || arg[len++] != '|');
	
	char *newarg = (char*)calloc(len+1, sizeof(char));
	memset(newarg, 0, len+1);
	
	FILE *fp = fopen("/var/restricted_cmd.txt", "r");
	if (fp > 0)
	{
		char command[maxColumns];
		while (fgets(command, sizeof(command), fp))
		{
			command[strlen(command) - 1] = '\0';
			char *p = strstr(argv[i], command);
			if(p == argv[i] || (p != NULL && p[-1] == ' '))
			{
				flag = 1;
				break;
			}
		}
		if(flag == 0)
			strncpy(newarg, arg, len);
		else
			newarg[0] = '';
	}
	fclose(fp);
	free(arg);
	return newarg;
}

char** init(int argc, char *argv[])
{
	char **newargv = (char**)calloc(argc, sizeof(char*));
	for(int i=0;i<argc;i++)
	{
		int len = strlen(argv[i]);
		char *newarg = sanitizeShellCode(argv[i]);
		newargv[i] = sanitizePathVulnerability(newarg);
	}
	return newargv;
}

char** init2(int argc, char *argv[])
{
	char **newargv = (char**)calloc(argc, sizeof(char*));
	for(int i=0;i<argc;i++)
	{
		int len = strlen(argv[i]);
		char *newarg = sanitizeShellCode(argv[i]);
		newarg = sanitizePathVulnerability(newarg);
		newargv[i] = sanitizeCommandInjection(newarg);
	}
	return newargv;
}

