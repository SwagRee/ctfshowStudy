a = {
    '001': {'name': '张三', 'age': 26, 'identity': '军人', 'score': 88},
    '002': {'name': '李四', 'age': 24, 'identity': '工人', 'score': 78},
    '003': {'name': '王五', 'age': 22, 'identity': '农民', 'score': 95},
    '004': {'name': '小明', 'age': 25, 'identity': '军人', 'score': 90}
}

for key in a:
    if a[key]['identity'] == '军人':
        a[key]['加分'] = 10
    else:
        a[key]['加分'] = 0

print("处理后的考生信息:", a)