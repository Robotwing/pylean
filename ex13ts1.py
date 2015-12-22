from sys import argv

script,user_name = argv

prompt = '>'

print "My name is %s, and you know I am the %s script." %(user_name,script)

print "do u like me?"

like = raw_input(prompt)

print "how old r u?"

age = raw_input(prompt)

print """

OK, you said you %r me very much. you r %r years old.

""" %(like,age)