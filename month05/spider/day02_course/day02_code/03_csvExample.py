"""
csv模块示例
"""
import csv

with open('fengyun.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['聂风', '血饮狂刀', '梦'])
    writer.writerow(['步惊云', '绝世好剑', '楚楚'])


f = open('fengyun.csv', 'a', newline='')
writer = csv.writer(f)
writer.writerow(['秦霜', '天霜拳', '孔慈'])
f.close()
















