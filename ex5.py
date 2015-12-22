#-*-coding: utf-8 -*-
#Python的格式化输入 %   
#%r 不管是什么都打印出来 repr()

name = 'Robotwing'
age = 20
height =188 #cm
weight = 160 #kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." %name
print "Let's talk about",name,"."



print "He's %r cm tall." %height
print "He's %d kg heavy." %weight
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." %(eyes,hair)
print "His teeth are usually %s depending on the coffee." %teeth

print "If I add %r, %r, and %r I get %d." % (age,height,weight,age+height+weight)
