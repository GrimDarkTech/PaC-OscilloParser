import threading
import typing

class ThreadManager:
    """Сlass for managing threads"""
    
    threads = [] 

    @staticmethod
    def create_thread(method, **kwargs):
        """Creates thread to execute method in new thread"""
        thread = threading.Thread(target=method, kwargs = kwargs)
        ThreadManager.threads.append(thread)

    @staticmethod
    def start_threads():
        """Starts all thread in threads list"""
        for thread in ThreadManager.threads:
            thread.start()

    @staticmethod
    def wait_for_threads():
        """Waits for threads complete all tasks"""
        for thread in ThreadManager.threads:
            thread.join()