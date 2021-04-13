#include "stdio.h"
#define OK 0
int x[100],bestx[100];
int cv = 0,cw = 0,mw = 0,mv = 0;
int c,n;
int weight[100];
int value[100];

int print()
{
	int m;
	for( m = 0;m<n;m++)
		printf("%d  ",bestx[m]);
	printf("\n背包中最大价值 :%d\n",mv);
	return OK;
}
int place(int t)
{
	if(cw+weight[t] > c)
		return 0;
	return 1;
}

void Track(int t)
{
	int m;
	if(t>=n)
	{
		if(cv>mv)
		{
			mv=cv;
			for(m = 0;m<n;m++)
				bestx[m] = x[m];
		}
	}
	else
	{
		for(m = 0;m<=1;m++)
		{
			x[t] = m;
			if(x[t] == 0)
			{
				Track(t+1);
				x[t] = 0;
			}
			else if(place(t) == 1 && x[t]==1)
			{

				cv = cv + value[t];
				cw = cw + weight[t];
				Track(t+1);
				x[t] = 0;
				cv = cv - value[t];
				cw = cw - weight[t];
			}
		}
	}
}

void main()
{
	int i;
	for(i = 0;i<100;i++)
	{
		x[i] = 0;
		bestx[i] = 0;
		weight[i] = 0;
		value[i] = 0;
	}
	printf("物品数量:");
	scanf("%d",&n);
	printf("背包容量:");
	scanf("%d",&c);
	printf("依次输入物品的重量:");
	for(i=0;i<n;i++)
		scanf("%d",(weight+i));
	printf("依次输入物品的价值:");
	for(i=0;i<n;i++)
		scanf("%d",(value+i));
	Track(0);
	print();
}
