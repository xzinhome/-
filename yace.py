import requests
import multiprocessing
import time

# 目标URL
TARGET_URL = "http://www.mayikt.vip"
# 并发数
CONCURRENCY = 100
# 每个进程的请求次数
REQUESTS_PER_PROCESS = 1000

def send_request(url, num_requests):
    for _ in range(num_requests):
        try:
            response = requests.get(url)
            print(f"Status Code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")

def stress_test(url, concurrency, requests_per_process):
    processes = []
    for _ in range(concurrency):
        p = multiprocessing.Process(target=send_request, args=(url, requests_per_process))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

if __name__ == "__main__":
    start_time = time.time()
    stress_test(TARGET_URL, CONCURRENCY, REQUESTS_PER_PROCESS)
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time} seconds")
