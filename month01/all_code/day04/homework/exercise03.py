"""
    商品优惠
    打折策略：如果vip客户，消费小于500,享受85折
                        否则享受8折
            否则，消费大于800,享受9折
                 否则原价
    根据账户类型和消费金额，计算折扣.
"""
account_type = input("请输入账户类型：")
money = float(input("请输入消费金额："))
if account_type == "vip":
    if money < 500:
        print("享受85折扣")
    else:
        print("享受8折扣")
else:
    if money > 800:
        print("享受9折扣")
    else:
        print("原价购买")
