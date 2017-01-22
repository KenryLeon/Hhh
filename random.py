#!\usr\bin\env python
# -*- coding:UTF-8 -*-

import random

a = random.choice(range(36))
b = random.choice(range(36))
c = random.choice(range(36))
d = random.choice(range(26,36))
e = random.choice(range(26,36))
f = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9']

print ('本轮中奖号码为：')
print ('\xe8\xb4\xb5'.decode('utf-8')+"A"+' '+f[a]+f[b]+f[c]+f[d]+f[e])
