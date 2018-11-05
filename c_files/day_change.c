#include<stdio.h>

static int daytab[2][13] = {
	{0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31},{0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31}
};
int day_of_year(int year, int month, int day)
{
	int lead,i;
	
	lead = (year%4 == 0 && year%100 != 0) || year%400 == 0;
	for(i =1; i < month; i++)
		day += daytab[lead][i];
	return year, day;
}
void month_day_year(int year, int day, int *pmonth, int *pday)
{
	int lead, i;
	
	lead = (year%4 == 0 && year%100 != 0) || year%400 == 0;
	for(i = 1; day > daytab[lead][i]; i++)
		day -= daytab[lead][i];
	*pmonth = i;
	*pday = day;
}
void main()
{
	int month, day;
	
	printf("%d\n", day_of_year(2018,9,8));
	month_day_year(2018, 257, &month, &day);
	printf("%d, %d\n", month, day);
}
