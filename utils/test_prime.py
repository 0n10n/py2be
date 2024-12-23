def is_prime(num: int) -> bool:
    """判断一个正整数是不是质数

    :param num: 正整数
    :return: 如果是质数返回True，否则返回False
    """
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return num != 1

if (is_prime(int(input()))):
    print("Is prime")
else:
    print("Not prime")

