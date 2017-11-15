#include <unistd.h>
#include <dirent.h>
#include <stdio.h>

int main(void)
{

	DIR *dir = opendir(".");

	struct dirent *dp ;

	while( ( dp = readdir(dir) ) != NULL )
	{
		printf("%s\n",dp->d_name);

	}

	return 0;

}
