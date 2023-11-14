class Queue:
    def __init__(self):
        self.__queue = []
    @property
    def queue(self):
        return self.__queue
    def push(self, el):
        print("Помещаем в очередь..", el)

        self.queue.append(el)
        # print(len(self.queue),": ",el)
        return
    def pop(self):
        try:
            el = self.queue.pop(0)
            print(f"Извлекаем из очереди..", el)
            return
        except IndexError:
            print("Ошибка! Очередь пуста!")
            return


q = Queue()

q.push(11)
q.push(22)

q.pop()
q.push(33)

q.pop()
q.pop()
q.pop()
