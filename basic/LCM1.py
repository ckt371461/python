def compute_hcf(x, y):
   while(y):
       # x, y = y, x % y
       t = x
       x = y
       y = t%y
   return x
def LCM (x,y):
    hcf = compute_hcf(x,y)
    return int(hcf*(x/hcf)*(y/hcf))
print(LCM(50,66))

