#
def avg(*args):
    length = len(args)
    total = sum(args)
    if length == 0:
        return 0
    else:
        return total/length
result = avg(1,2,3,4,5)
print(result)
#iot pj တွေမှာ အသုံးဝင် sensor ka nay data ဘလောက်ပို့မလဲဆိုတာမသိ
