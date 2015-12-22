#-*- coding:utf-8 -*-
#raw_input 将所有输入作为字符串看待，返回字符串类类型
#input()希望读取合法的python表达式，对纯数字输入有自己的特性

print "What's your name?",
name = input()

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old,%r tall and %r heavy." %(age,height,weight)
