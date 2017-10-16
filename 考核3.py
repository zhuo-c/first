# coding = utf-8
class Product:
    '''This is a class for the information of product. '''
    def __init__(self, number, name, price):
        self.number = number
        self.name = name
        self.price = price

def initDict(dict):
    fi = open("product.txt", "r")
    for line in fi.readline():
        lis = line.split(' ')
        lis[2] = lis[2][:-1]
        dict[lis[0]] = (lis[1], lis[2])
    fi.close()

def addProduct(prod, dict):
    '''用字典来存储商品'''
    dict[prod.number] = (prod.name, prod.price)

def delProduct(prod, dict):
    '''将商品从字典中删除'''
    del dict[prod.number]

def CashIn(dict):
    sum = 0
    '''打印小票'''
    fi = open('ticket.txt', 'w+')
    fi.truncate()
    while True:
        INPUT = input('请输入商品编号和数量，用空格隔开：')
        if not INPUT:
            fi.write('总价格：'+ str(sum))
            fi.close()
            return sum
        lis = INPUT.split(' ')
        print (lis)
        number = lis[0]
        shuliang = int(lis[1])
        sum += float (dict[number][1]) * shuliang
        fi.write('名称：'+ dict[number][0] + ' ' + '商品编号' + number + ' ')
        return sum

def reload(dict):
    fi = open('product.txt', 'w+')
    fi.truncate()
    for key in dict.key():
        fi.write(key + ' ' + dict[key][0] + ' ' + dict[key][1] + '\n')
    fi.close()

if __name__=='__main__':
    dict = {}
    initDict(dict)
    print('欢迎使用银行收银系统')
    print('1.添加新的商品入库')
    print('2.从库中删除已有商品')
    print('3.查看库中所有商品')
    print('4.收银并打印小票')
    print('5.结束并关闭系统')
    print('请输入对应序号实现功能：')

    while True:
        switch = int(input())
        if switch in range(1, 6):
            break
        else:
            print ("输入不符合规则，请重新输入：")
    while not switch == 5:
        if switch == 1:
            name = input("请输入商品名称：")
            number = input("请输入商品编号：")
            price = input("请输入商品价格：")
            product = Product(number, name, price)
            addProduct(product, dict)
            print ("成功!")
            switch = int(input("请输入对应序号实现功能："))
        elif switch == 2:
            number = input("请输入要删除商品编号：")
            product = Product(number, dict[number][0], dict[number][1])
            delProduct(product, dict)
            switch = int(input("请输入对应序号实现功能："))
        elif switch == 3:
            for key in dict.keys():
                print ("编号："+key, "名称："+dict[key][0], "价格："+dict[key][1])
            switch = int(input("请输入对应序号实现功能："))
        else:
            sum = CashIn(dict)
            print ("小票已经打印，总价格为："+str(sum))
            switch = int(input("请输入对应序号实现功能："))
    if switch == 5:
        reload(dict)

    
    
                 
                 
                 




        
