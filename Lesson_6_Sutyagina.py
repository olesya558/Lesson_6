# 1. Даны значения величины заработной платы заемщиков банка (zp)
# и значения их поведенческого кредитного скоринга (ks):
# zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110],
# ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832].
# Найдите ковариацию этих двух величин с помощью элементарных действий,
# а затем с помощью функции cov из numpy
# Полученные значения должны быть равны.
# Найдите коэффициент корреляции Пирсона с помощью ковариации
# и среднеквадратичных отклонений двух признаков,
# а затем с использованием функций из библиотек numpy и pandas.
import numpy as np
from math import sqrt
zp = [35, 45, 190, 200, 40, 70, 54, 150, 120, 110]
ks = [401, 574, 874, 919, 459, 739, 653, 902, 746, 832]
zp_avg = 101.4
ks_avg = 709.9
zp_cov1 = (zp[0] - zp_avg)
# -66.4
zp_cov2 = (zp[1] - zp_avg)
# -56.400000000000006
zp_cov3 = (zp[2] - zp_avg)
# 88.6
zp_cov4 = (zp[3] - zp_avg)
# 98.6
zp_cov5 = (zp[4] - zp_avg)
# -61.400000000000006
zp_cov6 = (zp[5] - zp_avg)
# -31.400000000000006
zp_cov7 = (zp[6] - zp_avg)
# -47.400000000000006
zp_cov8 = (zp[7] - zp_avg)
# 48.599999999999994
zp_cov9 = (zp[8] - zp_avg)
# 18.599999999999994
zp_cov10 = (zp[9] - zp_avg)
# 8.599999999999994

ks_cov1 = (ks[0] - ks_avg)
# -308.9
ks_cov2 = (ks[1] - ks_avg)
# -135.89999999999998
ks_cov3 = (ks[2] - ks_avg)
# 164.10000000000002
ks_cov4 = (ks[3] - ks_avg)
# 209.10000000000002
ks_cov5 = (ks[4] - ks_avg)
# -250.89999999999998
ks_cov6 = (ks[5] - ks_avg)
# 29.100000000000023
ks_cov7 = (ks[6] - ks_avg)
# -56.89999999999998
ks_cov8 = (ks[7] - ks_avg)
# 192.10000000000002
ks_cov9 = (ks[8] - ks_avg)
# 36.10000000000002
ks_cov10 = (ks[9] - ks_avg)
# 122.10000000000002

multi_1 = zp_cov1 * ks_cov1
multi_2 = zp_cov2 * ks_cov2
multi_3 = zp_cov3 * ks_cov3
multi_4 = zp_cov4 * ks_cov4
multi_5 = zp_cov5 * ks_cov5
multi_6 = zp_cov6 * ks_cov6
multi_7 = zp_cov7 * ks_cov7
multi_8 = zp_cov8 * ks_cov8
multi_9 = zp_cov9 * ks_cov9
multi_10 = zp_cov10 * ks_cov10
sum_multi = multi_1 + multi_2 + multi_3 + multi_4 + multi_5 + multi_6 + multi_7 + multi_8 + multi_9 + multi_10
covariance = sum_multi / 9
print(covariance)
# 10175.377777777778


d_zp = ((zp_cov1)**2 + (zp_cov2)**2 + (zp_cov3)**2 + (zp_cov4)**2 + (zp_cov5)**2 + (zp_cov6)**2 + (zp_cov7)**2 + (zp_cov8)**2 + (zp_cov9)**2 + (zp_cov10)**2) / 10
std_zp = sqrt(d_zp)
print(std_zp)
# 59.115480206118605

d_ks = ((ks_cov1)**2 + (ks_cov2)**2 + (ks_cov3)**2 + (ks_cov4)**2 + (ks_cov5)**2 + (ks_cov6)**2 + (ks_cov7)**2 + (ks_cov8)**2 + (ks_cov9)**2 + (ks_cov10)**2) / 10
std_ks = sqrt(d_ks)
print(std_ks)
# 174.55340157098058

Pearson_correlation_coefficient = covariance/(std_zp*std_ks)
print(Pearson_correlation_coefficient)
# 0.9861001023043512

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
cov1 = np.mean(zp*ks) - np.mean(zp) * np.mean(ks)
print(cov1)
covariance = np.cov(zp, ks, ddof=1)
print(covariance)
std_zp = np.std(zp)
print(std_zp)
std_ks = np.std(ks)
print(std_ks)
pearson = covariance/(std_zp*std_ks)
print(pearson)


# 2. Измерены значения IQ выборки студентов,
# обучающихся в местных технических вузах:
# 131, 125, 115, 122, 131, 115, 107, 99, 125, 111.
# Известно, что в генеральной совокупности IQ распределен нормально.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.
x = np.array([131, 125, 115, 122, 131, 115, 107, 99, 125, 111])
n = 10
# 1 -a = 95%
a = 5
# std - ?
# M - ?
# # критерий стьюдента
M = x.mean()
print(M)
variance = x.var(ddof=1)
print(variance)
std = sqrt(variance)
print(std)
t = 2.262
t_1 = M + ((t * std) / sqrt(n))
print(t_1)
# ответ 125.64339223691834
t_2 = M - ((t * std) / sqrt(n))
print(t_2)
# ответ 110.55660776308164

# 3. Известно, что рост футболистов в сборной распределен нормально
# с дисперсией генеральной совокупности, равной 25 кв.см. Объем выборки равен 27,
# среднее выборочное составляет 174.2.
# Найдите доверительный интервал для математического ожидания с надежностью 0.95.

from math import sqrt
std = 25
n = 25
M = 174.2
a = 5
z_kr = 1.96
confidence_interval_1 = M + (z_kr * sqrt(std)) / sqrt(n)
print(confidence_interval_1)
# 176.16
confidence_interval_2 = M - (z_kr * sqrt(std)) / sqrt(n)
print(confidence_interval_2)
# 172.23999999999998
