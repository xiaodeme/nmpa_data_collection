# -*- coding=utf-8 -*-



if __name__ == '__main__':


    # 方法一:
    a = [1,2,3]
    b = [1,2,4,5]
    print list(set(b).difference(set(a)))  # b中有而a中没有的
    print list(set(a).difference(set(b)))  # a中有而b中没有的


