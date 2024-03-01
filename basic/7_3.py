surprise=["Groucho","Chico","Harpo"]
surprise[-1]=surprise[-1].lower()
surprise[-1]=surprise[-1][::-1]#善用slice
surprise[-1]=surprise[-1].capitalize()
print(surprise)