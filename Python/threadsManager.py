import threading
import typing

class ThreadManager:
    """Сlass for managing threads"""
    
    treads = [] 

    @staticmethod
    def create_thread(method, file_number):
        thread = threading.Thread(target=method, kwargs={"file_number":file_number})
        ThreadManager.treads.append(thread)

    @staticmethod
    def start_threads():
        for thread in ThreadManager.treads:
            thread.start()

    @staticmethod
    def wait_for_threads():
        for thread in ThreadManager.treads:
            thread.join()