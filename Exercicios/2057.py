hs,tp,fs = map(int,input().split())
hrs = hs+tp+fs
if hrs>24:
    print(hrs-24)
elif hrs<0:
    print(hrs+24)
else:
    print(hrs)