# Python学习笔记~编程小哥令狐

[TOC]



# 一.Python运行发生情况

- 一个 `Python`程序是以 `.py`结尾的文件
- 一个 `Python`程序是通过 **Python解释器**来进行**读取**和**运行**的。

# 二.变量

## 2.1变量引入前说明

```python
message="Hello world"
print(message)

message="编程令狐"
print(message)
```

- 在程序中可以随时修改变量的值，Python始终记录变量的最新值。

## 2.2变量的命名和使用

规则：

1. 变量名不能以数字开头，只能以字母，数字，下划线组成。
2. 变量名不能包含空格
3. 不要使用关键字命名
4. 尽量使用小写字母命名变量名

## 2.3字符串

**字符串**：就是一系列字符

表示方法：被单引号或双引号包起来的内容

### 2.3.1使用方法修改字符串大小写

```python
#将字符串的首字母转换成大写，使用title（）方法
name="ada lovelace"
print(name.title())
print(name.upper())#转换成大写
print(name.lower())#转换成小写
```

### 2.3.2合并 拼接字符串

- 使用 **“+”**号进行直接拼接------**拼接法**

```python
first_name="ada"
last_name="lovelace"
full_name=first_name+" "+last_name#中间加了一个空格
print(full_name)
#print("Hello"+" "+full_name.title())
```



### 2.3.3使用制表符或换行来添加空白

- 制表符就是5个空格 `\t`

```python
print("\tPython")
```

- 换行符 `\n`

```python
print("languages:\npython\nC")
```

### 2.3.4删除空白

```python
favorite_language=' python '
print(favorite_language)

favorite_language.rstrip()
print(favorite_language)
name="\tJackiehao\n"
print(name.lstrip())
print(name.rstrip())#末尾没有空白
print(name.strip())

```

### 2.3.5双引号运用

- 字符串里面用双引号要加转义字符 `\`

```python
print("\nAlbert once said,\"Aperson ffff\"sss.")
```

## 2.4数字

### 2.4.1整数

- 整数可以做四则运算

- 用两个 `**`表示乘方

```python
Num_1=3**2
print(Num_1)
```

- 整数的除法

整数除法的结果只包含 **整数**，小数部分会删除

`//`表示Python3整数除法取整。

```python
print(5+3)
print(11-3)
print(4*2)
print(8//1)
```



### 2.4.2浮点数

- 带小数点的数字成为浮点数 **整数**部分，小数部分删除。

```python
3/2=1
```



```python
print(0.2+0.1)
#0.30000000000000004
```

### 2.4.3使用函数str（）避免类型错误

- 为什么要使用str()函数呢？

**因为23 是数字，也就是非字符串类型的，我们利用str将数字转换成字符型进行输出**

```python
age=23
message="happy"+str(age)+"rd Birthday!"
print(message)
```

如果用以下代码则会报错：

```python
age=23
message="happy"+age+"rd Birthday!"#没有str函数
print(message)
```

# 三.列表

## 3.1元素访问及其打印

- 这个列表非常类似于数组的含义，它是一种有序集合。

- l列表访问元素的方法与数组类似。
- 列表可以通过调用[-1]直接访问最后一个元素。

```python
bicycles=['trek','cannondable','redline','specialized']
#print(bicycles)
print(bicycles[0].title())
print(bicycles[-1])#访问最后一个元素


name=['张三','李四','郭伟','诸葛亮']
print(name[0])
print(name[1])
print(name[2])
print(name[3])

print("Happy"+name[0].title()+".")
print("Happy"+name[1].title()+".")
print("Happy"+name[2].title()+".")
print("Happy"+name[3].title()+".")
```

## 3.2修改，添加和删除元素

### 3.2.1修改列表元素

- 直接利用索引下标进行修改

```python
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles[0]='ducat'
print(motorcycles)
```

### 3.2.2添加元素

1. 在列表末尾添加元素

方法： `append()`

```python
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.append('ducat')
print(motorcycles)
```

1. ​	在列表中插入元素

方法：`insert()`

```python
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.insert(0,'docat')
print(motorcycles)
```

### 3.2.3删除元素

1. 方法 `del`

可以删除任意位置的元素

1. 方法 `pop()`

可以删除最末尾的元素，也可以删除任意位置元素

1. 方法 `remove()`，根据值删除元素

```python
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
```

```python
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

print(motorcycles.pop())
print(motorcycles.pop(0))#删除任意位置元素
print(motorcycles)
```

```python
motorcycles=['honda','yamaha','suzuki']
print(motorcycles)

motorcycles.remove('honda')
print(motorcycles)
```



- **什么时候使用del语句，什么时候使用Pop语句？**
  - 答案：如果你要删除一个元素，且不再用它，则用**del**语句；反之亦然。



## 3.3组织列表

### 3.3.1使用sort（）对列表进行永久性排序

- 按字母大小写顺序进行升序排列/逆序排列【永久性的】

```python
cars=['bmw','audi','toyota','subaru']
升序排列：
cars.sort()
print(cars)

逆序排列：
cars.sort(reverse=True)
print(cars)
```

- 临时性的排序

```python
cars=['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)

print("Here is the sorted list:")
print(sorted(cars))

print("Here is the original list again:")
print(cars)
```

### 3.3.2倒着打印列表/永久性排列

利用方法： `Reverse()`

```python
cars=['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)
```



### 3.3.3确定列表长度

方法：`len（）`

```python
cars=['bmw','audi','toyota','subaru']
print(len(cars))
```

# 四、操作列表



## 4.1快速入门

- 循环列表 **magicans**执行操作后，将其打印在新变量 **magican**，在打印一遍新变量

```python
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician)
```

## 4.2缩进代码与循环操作

- for循环语句以下的缩进代码会被循环执行操作，没有缩进的代码不会被循环操作

```python
magicians=['alice','david','carolina']
for magician in magicians:
    print(magician.title()+",that was a great trick")
    print("I can not wait to see your next trick,"+magician.title()+"\n")
#这行代码没有缩进所以不会被循环操作
print("I can not wait to see your next trick,"+magician.title()+"\n")
```

## 4.3创建数值列表

- 方法： `Range（）`
- 循环打印数字不是从1到5，而是从1到4！！！

```python
for value in range(1,5):
    print(value)
```

### 4.3.1使用range()创建数字列表

- 使用 `list()`将 `range()`结果转换为列表。

```python
numbers=list(range(1,6))
print(numbers)

numbers=list(range(2,11,2))
print(numbers)

squares=[]
for value in range(1,11):
    square=value**2
    squares.append(square)

print(squares)
```

### 4.3.3数字统计计算/最大值/最小值/求和

```python
digits=[1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))
```

### 4.3.4列表解析

- 先遍历赋值在乘方

```python
squares=[value**2 for value in range(1,11)]
print(squares)
```

## 4.4使用列表的一部分

### 4.4.1切片

切片就是列表的一部分内容元素。

- 获取列表的2~4个元素

```python
motorcycles=['honda','yamaha','suzuki','name','fff']
print(motorcycles[1:4])

```

- 获取列表从表头开始

```python
motorcycles=['honda','yamaha','suzuki','name','fff']
print(motorcycles[:4])
```

- 获取列表从表尾结束

```python
motorcycles=['honda','yamaha','suzuki','name','fff']
print(motorcycles[2:])
```

### 4.4.2遍历切片

 **方法：** `for`循环+切片

#   五、if语句

## 5.1引入例子

```python
cars=['audi','bmw','subaru','toyota']

for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
```

## 5.2条件测试

- 每条if语句的核心就是一个值 `true`或 `false`。

### 5.2.1检查多个条件

1. 使用 **and**检查多个条件，相当于“&&”

```python
age_0=22
age_1=18
print(age_0>=21 and age_1>21)

```

1. 使用 **or**检查多个条件，相当于“||”

```python
age_0=22
age_1=18
print(age_0>=21 or age_1>21)

```

### 5.2.2检查特定值是否包含在列表中

- 关键字 `in` 

```python
requested_toppings=['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)

```

- 在if语句中，缩进的作用与for循环中相同，如果测试通过了，将执行if语句后面所有缩进的代码，否则将忽略他们。



### 5.3.2if-else语句

```python
age=17
if age>=18:
    print("you are oil enough to vote")
    print("you are oil enough to vote123456")
else:
    print("sorry you can   ")
    print("sorry you can  please register ")

```

### 5.3.3if-elif-else

```python
age=12

if age<4:
    print("your admission cost is 0$")
elif age<18:
    print("your admission cost is 5$")
else:
    print("your admission cost is 0$")
```

### 5.3.4使用多个elif代码块

```python
age=12

if age<14:
    price=0
elif age<18:
    price=5
elif age<65:
    price=10
else:
    price=5
print("your admission cost is $"+str(price)+".")
```

# 六、字典

- 字典就是能够存储互不相联的信息

```python
alien_0={'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
```

##  6.2使用字典

-  **字典**是一系列的 **键------值对** 组成的。我们可以通过键访问值，也可以通过值访问键。

### 6.2.1访问字典中的值

```python
alien_0={'color':'green','points':5}
new_points=alien_0['points']
print("you just earned "+str(new_points)+"points!")
```

### 6.2.2添加键值对

- 字典是一种动态结构，可以随时添加键值对。

```python
alien_0={'color':'green','points':5}
print(alien_0)

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)

```

### 6.2.3创建空字典

```python
alien_0={}

alien_0['color']='green'
alien_0['points']=5
print(alien_0)
```

### 6.2.4修改字典中的值

```python
alien_0={'color':'green'}
print("The alien is"+alien_0['color']+".")

alien_0['color']='yellow'
print("The alien is now"+alien_0['color']+".")
```

```python
alien_0={'x_position':0,'y_position':25,'speed':'medium'}
print("Original x-position:"+str(alien_0['x_position']))

#向右移动外星人
#据外星人当前速度决定其移动多远
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    #这个外星人的移动速度一定很快
    x_increment=3
#新位置等于老位置加上增量
alien_0['x_position']=alien_0['x_position']+x_increment
print("New x-position:"+str(alien_0['x_position']))
```

### 6.2.5删除键值对

```python
alien_0={'color':'green','points':5}
print(alien_0)

del alien_0['points']
print(alien_0)
```

### 6.2.6由类似对象组成的字典

```python
favorite_languagres={
    'jen':'python',
    'sarah':'C',
    'edward':'ruby',
    'phil':'python',

}
print("Saras facorite language is"+favorite_languagres['sarah'].title()+".")
```

## 6.3遍历字典

### 6.3.1遍历所有的键值对

-  `items()`方法可以返回字典里的键和值得元素

```python
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for key,value in user_0.items():
    print("\nkey:"+key)
    print("value:"+value)
```

### 6.3.2遍历字典中的所有键

- 在不需要使用字典中的值时，方法 `key（）`很有用。遍历所有键值。

```python
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',

}
for name in favorite_languages.keys():
    print(name.title())
```

```python
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',

}
friends=['phil','sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("Hi"+name.title()+",I see your favorite languages is"+favorite_languages[name].title()+"!")
```

### 6.3.3按顺序遍历字典中的所有键

```python
favoirte_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
for name in sorted(favoirte_languages.keys()):
    print(name.title()+",thank you for taking the poll")
```

### 6.3.4遍历字典中的所有值

```python
favoirte_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}
print("The following languages have been menthioned:")
for language in favoirte_languages.values():
    print(language.title())
```



## 6.4嵌套

- 将字典存储在列表中叫做 **嵌套**

### 6.4.1字典列表

```python
#字典
alien_0={
    'color':'green',
    'points':5,
}
alien_1={
    'color':'red',
    'points':15,
}
alien_2={
    'color':'yellow',
    'points':25,
}
aliens=[alien_0,alien_1,alien_2]#列表
for alien in aliens:
    print(alien)
```

### 6.4.2在字典中存储列表

```python
pizza={
    'crust':'thick',
    'toppings':['mushrooms','extra cheese'],
}

print("you ordered a "+pizza['crust']+"-crust pizza"+"with the following toppings:")

for topping in pizza['toppings']:
    print("\t"+topping)
```

### 6.4.3在字典中存储字典

```python
users={
    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princetion',
    },
    'mucire':{
        'first':'marie',
        'last':'curie',
        'location':'princetion',
    },
}
for username,user_info in users.items():
    print("\nusername:"+username)
    full_name=user_info['first']+" "+user_info['last']
    location=user_info['location']

    print("\tFull name:"+full_name.title())
    print("\tLocation:"+location.title())
```

# 7、用户输入和while循环



## 7.1函数input

- 这是一个输入函数

```python
message=input("tell me something and I will repeat it back to you:")
print(message)
```

|                                                              |
| ------------------------------------------------------------ |
| ![](https://cdn.jsdelivr.net/gh/JackieLing/mage1/img/20200815185347.png) |

### 7.1.1编写清晰的程序

```python
name=input("please enter your name:")
print("Hello"+name+"!")
```

### 7.1.2使用int（）来获取数值输入

-  `int()`可以将字符串转换成数字

```python
age=input("How old are you?")
age=int(age)
if age>18:
    print("\n you are tall enough to ride")
else:
    print("\n you .....")
```

### 7.1.3求模运算符

```python
number=input("Enter a number ,and I will tell you if it is even or odd")
number=int(number)

if number%2==0:
    print("\nThe number"+str(number)+"is even")
else:
    print("\nThe number "+str(number)+"is odd")
```

