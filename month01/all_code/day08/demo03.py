"""
    函数相互调用
"""
# -------------函数---------------
def attack():
    print("直拳") 
    return "ok"

def repeated_attack(count):
    list_result = []
    for i in range(count):
        result = attack()
        list_result.append(result)
    return list_result

# -------------入口---------------
res = repeated_attack(1)
print(res)  #
