#coding=utf-8

#tuple是元组的意思，和list很像。不过元组中的字符串或者叫对象是不可变的！定义的方式看下面的代码

zoo=('wolf','elephant','penguin')
print 'Number of animal in zoo is ',len(zoo)

new_zoo=('monkey','dolphin',zoo)
print 'Number of animal in the new zoo is',len(zoo)
print 'All animal in new zoo are',len(new_zoo)
print 'Animal also brought from old zoo are',new_zoo[2]
print 'Last animal brought from old zoo is',new_zoo[2][2]

#这里要注意的是，在列表、元组和字典中可以嵌套列表、元组和字典。。定义元组的方式是（''）   元组是不可以修改内容的！！
#new_zoo[2][2]是查第三个项目的第三个项目！这样的方式适用于列表和字典吗？
#如果定义的元组中只有一个项目的话也需要加入都好即：name=('wangkai',)      定义空元组则不需要eg：name=()即可