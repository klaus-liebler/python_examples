import re

regex = r"^(\+\d+ |0)([1-9]\d+) ([1-9]\d*)(\-\d{1,}|)$"

telefoneRegex= re.compile(regex)
test1 = "+438*58d434-wer"
result = telefoneRegex.search(test1)
print(result)
test1 = "+49 541 9695-152"
result = telefoneRegex.search(test1)
print("Die Ortsvorwahl ist", result.group(2))


