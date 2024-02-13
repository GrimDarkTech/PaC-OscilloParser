import threading
import typing

class ThreadManager:
    """Сlass for managing threads"""
    
    treads = [] 

    @staticmethod
    def create_thread(method, **kargs):
        """"""
        thread = threading.Thread(target=method, kwargs = kargs)
        ThreadManager.treads.append(thread)

    @staticmethod
    def start_threads():
        for thread in ThreadManager.treads:
            thread.start()

    @staticmethod
    def wait_for_threads():
        for thread in ThreadManager.treads:
            thread.join()