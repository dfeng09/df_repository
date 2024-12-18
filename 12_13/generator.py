import time, psutil, random, os
random_num = [i**2 for i in range(10)]
#列表推导式
list_start_time, liststart_mem = time.time(), psutil.Process(os.getpid()).memory_info().rss//1024//1024
num_list = [random.choice(random_num) for _ in range(10**6)]
list_end_time, listend_mem = time.time(), psutil.Process(os.getpid()).memory_info().rss//1024//1024
print(f"list_time: {list_end_time - list_start_time}, list_mem: {listend_mem - liststart_mem}")
#生成器表达式
list_start_time, liststart_mem = time.time(), psutil.Process(os.getpid()).memory_info().rss//1024//1024
num_list = (random.choice(random_num) for _ in range(10**6))
list_end_time, listend_mem = time.time(), psutil.Process(os.getpid()).memory_info().rss//1024//1024
print(f"list_time: {list_end_time - list_start_time}, list_mem: {listend_mem - liststart_mem}")

# 处理大数据集：如逐行读取超大文件。
# 无限序列生成：如生成斐波那契数列或素数。
# 流式数据处理：如实时处理网络数据。