#include <stdio.h>
#include <sys/stat.h>

int main(int argc, char *argv[])
{
	FILE *fp = fopen(argv[1], "rb");
	if( NULL == fp)
	{
		printf("Open file fail!\n");
		return -1;
	}

	struct stat fileStat;
	stat(argv[1], &fileStat);
	//printf("File '%s' length:%d\n", argv[1], fileStat.st_size);

	unsigned char *pucBuff = malloc(fileStat.st_size);
	memset(pucBuff, 0, fileStat.st_size);
	fread(pucBuff, sizeof(unsigned char),  fileStat.st_size, fp);
	fclose(fp);

	unsigned char ucCheckSum = 0;
	unsigned int i = 0;
	for(i = 0; i < fileStat.st_size; ++i)
		ucCheckSum += pucBuff[i];
	free(pucBuff);

	printf("File '%s' checksum:0x%X\n", argv[1], ucCheckSum);

	return 0;
}
