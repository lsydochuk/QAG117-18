# Нужно написать функцию, которая позволит Вам конвертировать указанное Вами число секунд в формат записи дни:часы:минуты:секунды
a = int(input())
def d_h_m_s():
    print(str(d) + ':' + str(h) + ':' + str(m) + ':' + str(s))
d = a//86400
if a >= 86400:
    a = a - (d * 86400)
h = a//3600
m = (a//60) % 60
s = a % 60
if m < 10:
    m = str('0' + str(m))
else:
    m = str(m)
if s < 10:
    s = str('0' + str(s))
else:
    s = str(s)

d_h_m_s()