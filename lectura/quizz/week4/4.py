def triangle(a,b,c):
    if a+b>c and a-b<c and a+c>b and a-c<b and b+c>a and b-c<a:
        print("YES")
    else:    
        print("NO")

triangle(565,34,800)