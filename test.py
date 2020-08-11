from threading import Timer

class MyClass(object):
    def _init_(self):
        self.iteration_count = 0
        self.heartbeat = 1

    @staticmethod
    def print_msg():
        print ("hello world!")

    def start_job(self):
        self.print_msg()
        self.iteration_count += 1
        print(self.iteration_count)

        timer = Timer(
            interval=self.heartbeat,
            function=self.start_job,
        )
        timer.start()

        if self.iteration_count >= 10:
            timer.cancel()

MyClass().start_job()