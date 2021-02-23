"""
execjs模块用法
"""
import execjs

with open('translate.js', 'r') as f:
    jscode = f.read()

jsobj = execjs.compile(jscode)
sign = jsobj.eval('e("girl","320305.131321201")')
print(sign)
















