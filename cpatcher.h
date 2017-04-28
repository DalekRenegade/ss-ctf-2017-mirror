#include<stdio.h>
#include<stdlib.h>
#include<string.h>

char** init(int argc, char *argv[])
{
  char **newargv = (char**)calloc(argc, sizeof(char*));
  for(int i=1;i<argc;i++)
  {
    int len = strlen(argv[i]);
    newargv[i] = (char*)malloc(len+1);
    strncpy(newargv[i], argv[i], len);
    newargv[i][len+1]='\0';
  }
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

int checkEnvironmentVaraible(int argc, char *argv[])
{

}

int checkPathVulnerbility(int argc, char *argv[])
{
  int flag = 0;
  for(int i=1;i<argc;i++)
  {
    if(strstr(argv[i], "../") != NULL || argv[i][0] == '~')
    {
      flag = 1;
      break;
    }
  }
  return flag;
}

int checkSymlink(int argc, char *argv[])
{
  int flag = 0;
  for(int i=1;i<argc;i++)
  {
    if(strstr(argv[i], "../") != NULL)
    {
      flag = 1;
      break;
    }
  }
  return flag;
}
