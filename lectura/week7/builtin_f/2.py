a = input("")

Upper = sum(map(lambda x: x.isupper(), a))
Lower = sum(map(lambda x: x.islower(), a))

print(f"upper: {Upper}, lower: {Lower}")