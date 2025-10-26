def isOdd(num):
    # 先判断是否为整数类型，再判断是否为奇数
    return isinstance(num, int) and num % 2 != 0

# 测试示例
print(isOdd(3))    # 输出：True
print(isOdd(4))    # 输出：False
print(isOdd(3.5))  # 输出：False
print(isOdd("3"))  # 输出：False
