import hashlib
import multiprocessing
from multiprocessing import Pool, Manager

target_hash = '084BBE17CEC67E1D138F01A54D650F8D'.upper()
DIGITS = 10  # 查找10位数字
WORKERS = 10  # 使用10个核心


def check_range(args):
    start, end, found_event = args
    for num in range(start, end + 1):
        # 如果其他进程已经找到结果，提前终止
        if found_event.is_set():
            return None

        # 生成10位数字字符串（包含前导零）
        s = str(num).zfill(DIGITS)
        hashed = hashlib.md5(s.encode('utf-8')).hexdigest().upper()

        if hashed == target_hash:
            found_event.set()
            return s
    return None


if __name__ == '__main__':
    # 计算总范围
    total_numbers = 10 ** DIGITS
    chunk_size = total_numbers // WORKERS

    # 生成任务范围
    tasks = []
    manager = Manager()
    found_event = manager.Event()

    for i in range(WORKERS):
        start = i * chunk_size
        end = (i + 1) * chunk_size - 1 if i < WORKERS - 1 else total_numbers - 1
        tasks.append((start, end, found_event))

    # 启动进程池
    with Pool(processes=WORKERS) as pool:
        results = pool.imap_unordered(check_range, tasks)

        # 等待第一个有效结果
        for result in results:
            if result is not None:
                print(f"\n找到匹配的数字：{result}")
                found_event.set()
                pool.terminate()
                break
        else:
            print("未找到匹配的数字")