marks = {}.fromkeys(['Math','English','Science'],0)
print(marks)
for item in marks.items():
	print(item)

print(list(sorted(marks.keys())))
