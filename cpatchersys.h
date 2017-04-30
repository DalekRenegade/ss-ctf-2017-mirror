#include<stdio.h>
#include<stdlib.h>
#include<string.h>

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
