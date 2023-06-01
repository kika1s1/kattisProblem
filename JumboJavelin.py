n = int(input())
collections = []
for i in range(n):
    x = int(input())
    collections.append(x)
print(sum(collections) - (len(collections)-1))
    