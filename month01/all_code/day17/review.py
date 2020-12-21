"""
    迭代器
        class 可迭代对象:
            def __iter__(self):
                return 迭代器()

        class 迭代器:
            def __next__(self):
                return 数据

        # for 变量 in 可迭代对象:
        #     print(变量) # 得到的是迭代器返回的数据

        iterator = 可迭代对象.__iter__()
        while True:
            try:
                变量 = iterator.__next__()
                print(变量)
            except StopIteration:
                break

    def 函数名():
        ...
        yield 数据
        ...

    # class 生成器:
    #     def __iter__(self):
    #         return self
    #
    #     def __next__(self):
    #         return 数据

    # 调用函数不执行,而是返回生成器对象
    结果 = 函数名()
    # 通过for循环内部调用__next__函数,执行生成器函数.
    for item in 结果:
        print(item)

"""