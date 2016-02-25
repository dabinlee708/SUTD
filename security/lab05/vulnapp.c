/*
 * Vulnapp. Vulnerable app for buffer overflow testing.
 *
 * usage: 
 *      echo hello | ./vulnapp
 *      ./vulnapp < hello.txt
 * 
 * To compile:
 * 	Run ./make_vulnapp
 * 
 * Copyright 2004 by Feckless C. Coder, PhD.
 */

#include <stdio.h>
#include <string.h>
#define INPUT_BUFFER 64 /* maximum name size */

/*
 * read input, copy into s
 * gets(is insecure and prints a warning
 * 	so we use this instead
 */
void getlines(char *s)
{
	int c;
	while ((c=getchar())!=EOF)
		*s++ = c;
	*s = '\0';
}

/*
 * convert newlines to nulls in place
 */
void purgenewlines(char *s)
{
	int l;
	l = strlen(s);
	while(l--)
		if (s[l] == '\n')
			s[l] = '\0';
}

int main()
{
	char input[INPUT_BUFFER];
	getlines(input);

	if(strlen(input)<INPUT_BUFFER){
		purgenewlines(input);
		printf("Your text is: %s\n",input);
	}
	return 0;
}


