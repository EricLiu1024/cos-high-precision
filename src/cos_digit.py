from decimal import Decimal, getcontext

def cos_digit(a_str, n):
    """
    返回 cos(a) 的小数点后第 n 位数字
    a_str: 字符串形式的浮点数（弧度）
    n: 想要的小数位数（正整数）
    """

    # 1. 设置高精度：n + 50 位安全位
    getcontext().prec = n + 50

    # 2. 把输入转成 Decimal（不能用 float，会损失精度）
    a = Decimal(a_str)

    # 3. 泰勒展开初始化
    term = Decimal(1)   # 第 0 项
    s = Decimal(0)
    k = 0

    # 4. 递推计算 cos(a)
    # term_k+1 = term_k * (-a^2) / ((2k+1)(2k+2))
    threshold = Decimal(10) ** Decimal(-(n + 5))

    while True:
        s += term
        k += 1
        term *= -a * a / Decimal((2*k - 1) * (2*k))

        if abs(term) < threshold:
            break

    # 5. 转成字符串
    s_str = format(s, 'f')

    # 6. 分离整数和小数部分
    if '.' in s_str:
        int_part, frac_part = s_str.split('.')
    else:
        frac_part = ""

    # 7. 小数部分补齐
    frac_part = frac_part.ljust(n, '0')

    # 8. 返回第 n 位（注意下标从 0 开始）
    return frac_part[n - 1]


def main():
    a_str, n_str = input("请输入 a 和 n，用空格分隔: ").split()
    n = int(n_str)
    print(cos_digit(a_str, n))


if __name__ == "__main__":
    main()
