#include<stdio.h>
main()
{
	int m,n,i,j,a[10][10];
	printf("enter m value");
	scanf("%d",&n);
	printf("enter n value");
	scanf("%d",&m);
	for(i=0;i<m;i++){
		for(j=0;j<n;j++)
		{
			scanf("%d\t",&a[i][j]);	
		}	
	}
	printf("\nGiven Matrix\n");
	for(i=0;i<m;i++){
		for(j=0;j<n;j++)
		{
			printf("%d\t",a[i][j]);	
		}
		printf("\n");	
	}
	printf("Transpose of a matrix\n");
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d\t",a[j][i]);	
		}
		printf("\n");	
	}
	printf("\nReverse of a matrix\n");
	for(i=0;i<m;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d\t", a[j+1][i]);
		}
		printf("\n");
	}
}
