#include<stdio.h>
#include "csanitizer.h"

int main(int argc, char *argv[])
{
	argv = init2(argc, argv);
	printf("\n#%s#\n\n", argv[1]);
	return 0;
}
