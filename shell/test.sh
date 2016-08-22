#!/bin/bash
var=0
fun()
{
	var=1
}
 
fun
echo $var
mv test.txt test.txt.bak
echo $?
