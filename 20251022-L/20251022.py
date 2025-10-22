emra = ['filan', 'fisteku', 'tjeter', 'aaaaaa', 'zzzzzz']

emra.append("drin")
emra.extend(emra)
emra.remove("drin")
emra.pop()


print(emra)
print(len(emra))
print(max(emra))
print(min(emra))
print(list(emra))
