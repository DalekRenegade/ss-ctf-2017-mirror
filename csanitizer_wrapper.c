#include<stdio.h>
#include<unistd.h>
#include<libgen.h>
#include<csanitizer.h>

int main(int argc, char *argv[])
{
	argv = init(argc, argv);
	if(checkShellCode(argc, argv) > 0 || checkPathVulnerability(argc, argv) > 0 || checkCommandInjection(argc, argv) > 0)
	{
		printf("Sorry... You can't P00P on our service...\n");
		return 1;
	}
	
	extern char **environ;
	
	char *dupPath, *fileName;
	
	char *path = "{0}";
	
	dupPath = strdup(path);
	fileName = basename(dupPath);
	strcpy(argv[0], fileName);
	
	execve(path, argv, environ);
	
	return 0;
}
