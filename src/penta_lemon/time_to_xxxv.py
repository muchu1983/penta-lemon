import time
import random

def get_yao_number():
    """
    以当前时间为种子，生成 6 7 8 9 随机数
    6=老阴 7=少阳 8=少阴 9=老阳
    """
    # 用时间戳+微妙级时间做种子，增加离散度
    seed = int(time.time() * 1000000)
    print(time.time())
    random.seed(seed)
    
    # 限定只在 6,7,8,9 里随机
    return random.choice([6, 7, 8, 9])

# 测试：生成一爻
if __name__ == "__main__":
    num = get_yao_number()
    print("当前生成爻数：", num)
    
    # 一次性生成初始6个爻
    six_yao = [get_yao_number() for _ in range(6)]
    print("初始六爻数字(6789)：", six_yao)
