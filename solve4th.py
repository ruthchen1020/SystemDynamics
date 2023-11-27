from sympy import symbols, Eq, solve, I, re, im

class solve4th:
    def __init__(self,m1, k1, b1, m2, k2, b2):

        self.a4 = m1*m2
        self.a3 = b1*m2+b2*m2+b2*m1
        self.a2 = k2*m1+b1*b2+k1*m2+k2*m2
        self.a1 = k2*b1+b2*k1
        self.a0 = k1*k2
    # 创建符号变量
    def wn_and_damp(self):
        lambda_ = symbols('lambda')

        # 定义特征方程
        char_eq = Eq(self.a4 * lambda_**4 + self.a3 * lambda_**3 + self.a2 * lambda_**2 + self.a1 * lambda_ + self.a0, 0)

        # 解特征方程，获得特征值
        solutions = solve(char_eq, lambda_)

        # 打印特征值
        for solution in solutions:

            # 提取实部和虚部
            real_part = re(solution)
            imaginary_part = im(solution)

            # 计算自然频率
            natural_frequency = abs(solution)

            # 计算阻尼比
            damping_ratio = -real_part / natural_frequency
            # print('wn=',natural_frequency.evalf(),'damp=',damping_ratio.evalf())
        return(natural_frequency.evalf(),damping_ratio.evalf())

