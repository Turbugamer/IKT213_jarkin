from SIFT_FLANN import SIFT_FLANN_Matcher
from ORB_BF import ORB_BF_Matcher
import tracemalloc
import time
import psutil
import threading


class CPUMonitor:
    def __init__(self):
        self.cpu_usage = []
        self.monitoring = False
        
    def start_monitoring(self):
        self.cpu_usage = []
        self.monitoring = True
        thread = threading.Thread(target=self._monitor_cpu)
        thread.daemon = True
        thread.start()
        
    def stop_monitoring(self):
        self.monitoring = False
        
    def _monitor_cpu(self):
        while self.monitoring:
            cpu_percent = psutil.cpu_percent(interval=0.1)
            self.cpu_usage.append(cpu_percent)
            
    def get_stats(self):
        if not self.cpu_usage:
            return 0, 0
        avg_cpu = sum(self.cpu_usage) / len(self.cpu_usage)
        peak_cpu = max(self.cpu_usage)
        return avg_cpu, peak_cpu


def ORB_BF_main(dataset_path, results_folder):
    orb_bf_matcher = ORB_BF_Matcher()
    orb_bf_matcher.process_dataset(dataset_path, results_folder)
    
def SIFT_FLANN_main(dataset_path, results_folder):
    sift_flann_matcher = SIFT_FLANN_Matcher()
    sift_flann_matcher.process_dataset(dataset_path, results_folder)
    

data_orb_bf = r"Fingerprint_matching/dataset_folder/UiA"
data_sift_flann = r"Fingerprint_matching/dataset_folder/UiA"
results_folder = r"Fingerprint_matching/dataset_folder/results"

cpu_monitor = CPUMonitor()

tracemalloc.start()
cpu_monitor.start_monitoring()
start_time = time.time()
SIFT_FLANN_main(data_sift_flann, results_folder)
end_time = time.time()
cpu_monitor.stop_monitoring()

avg_cpu, peak_cpu = cpu_monitor.get_stats()
print(f"SIFT_FLANN processing time: {end_time - start_time:.2f} seconds")
print(f"SIFT_FLANN CPU usage - Average: {avg_cpu:.2f}%, Peak: {peak_cpu:.2f}%")

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 10**6:.2f}MB; Peak was {peak / 10**6:.2f}MB")
tracemalloc.stop()

print("-" * 50)

cpu_monitor = CPUMonitor()

tracemalloc.start()
cpu_monitor.start_monitoring()
start_time = time.time()
ORB_BF_main(data_orb_bf, results_folder)
end_time = time.time()
cpu_monitor.stop_monitoring()

avg_cpu, peak_cpu = cpu_monitor.get_stats()
print(f"ORB_BF processing time: {end_time - start_time:.2f} seconds")
print(f"ORB_BF CPU usage - Average: {avg_cpu:.2f}%, Peak: {peak_cpu:.2f}%")

current, peak = tracemalloc.get_traced_memory()
print(f"Current memory usage: {current / 10**6:.2f}MB; Peak was {peak / 10**6:.2f}MB")
tracemalloc.stop()