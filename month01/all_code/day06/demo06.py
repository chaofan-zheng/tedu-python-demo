"""
    字典推导式
"""

dict01 = {
    item:item **2 for item in range(10)
    if item % 3 ==0
}
print(dict01)
