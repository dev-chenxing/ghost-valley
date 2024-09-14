from typing import Union
import re

小寫數字表 = "零一二三四五六七八九"
小寫位名表 = "十百千"
組名表 = "萬億兆京垓秭穰溝澗正載"


def 中文数字(
    n: Union[int, float, str], 两: bool = False
) -> str:
    if 两 and n == 2:
        return "两"

    位名表 = 小寫位名表
    數字表 = 小寫數字表
    數字表 = 數字表
    點 = "点"

    n: str = str(n)
    i: str = n
    d = ""

    if "." in n:
        i, d = n.split(".", 1)
        d = d.rstrip("0")
    cn = ""
    i = list(reversed(i))

    def 轉中文數字(i):
        cn = ""
        for pos, digit in enumerate(i):
            位名 = ""
            if (digit != "0") and (pos > 0):
                位名 = 位名表[pos - 1]
                cn = 數字表[int(digit)] + 位名 + cn
            elif (pos == 0):
                cn = 數字表[int(digit)] + cn
            elif (digit == "0"):
                cn = 數字表[int(digit)] + cn
        return cn

    for pos, 一組阿拉伯數字 in enumerate(
        [i[idx: idx + 4] for idx in range(0, len(i), 4)]
    ):
        _cn = 轉中文數字(一組阿拉伯數字)
        if pos > 0:
            _cn = _cn + 組名表[pos - 1]
        cn = _cn + cn
    # 一萬零零六十零 -> 一萬零六十零
    cn = re.sub("零+", "零", cn)
    # 一萬零六十零 -> 一萬零六十
    cn = re.sub("(.)零$", r"\1", cn)
    # 一十六 -> 十六
    cn = re.sub("^一十", "十", cn)
    # 十零萬 -> 十萬
    cn = re.sub(f"([{位名表}])零([{組名表}])", r"\1\2", cn)
    if d != "":
        cn += 點 + d.translate(str.maketrans("0123456789", 數字表))
    return cn
