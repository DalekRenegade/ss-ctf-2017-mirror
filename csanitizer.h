#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char** init(int argc, char *argv[])
{
	char **newargv = (char**)calloc(argc + 1, sizeof(char*));
	newargv[0] = (char*)calloc(255, sizeof(char));
	for(int i=1;i<argc;i++)
	{
		int len = strlen(argv[i]);
		newargv[i] = (char*)calloc(len+1, sizeof(char));
		strncpy(newargv[i], argv[i], len);
		newargv[i][len]='\0';
	}
	newargv[argc] = (char *)0;
	return newargv;
}

int checkShellCode(int argc, char *argv[])
{
	int flag = 0;
	for(int i=1;i<argc;i++)
	{
		//NOPS, XOR, PUSH, MOV(register), MOV(constant)
		if(strstr(argv[i], "x90") != NULL || strstr(argv[i], "x31") != NULL || strstr(argv[i], "x68") != NULL || strstr(argv[i], "x89") != NULL || strstr(argv[i], "xb0") != NULL)
		{
			flag = 1;
			break;
		}
	}
	return flag;
}

int checkPathVulnerability(int argc, char *argv[])
{
	int flag = 0;
	for(int i=1;i<argc;i++)
	{
		if(strstr(argv[i], "../") != NULL || strstr(argv[i], "..\\") != NULL || strstr(argv[i], "..") == argv[i] || argv[i][0] == '~')
		{
			flag = 2;
			break;
		}
	}
	return flag;
}

int checkCommandInjection(int argc, char *argv[])
{
	int flag = 0;
	for(int i=1;i<argc;i++)
	{
		//Command chaining
		if(strstr(argv[i], ";") != NULL || strstr(argv[i], "&") != NULL || strstr(argv[i], "|") != NULL)
		{
			flag = 3;
			break;
		}
		else if(strstr(argv[i], "%n") != NULL || strstr(argv[i], "%hhn") != NULL)
		{
			flag = 5;
			break;
		}
		else
		{
			//Command injecting
			int maxColumns = 20;
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
						flag = 4;
						break;
					}
				}
			}
			fclose(fp);
		}		
	}
	return flag;
}
