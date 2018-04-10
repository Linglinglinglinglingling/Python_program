from Study.ADT.queue import Queue

class Master:

    def __init__(self):
        self.queue=Queue()
        self.agent_id=0

    def status(self):
        return self.queue.the_queue[self.queue.front:]

    def __str__(self):
        return str(self.status())

    def enter(self):
        self.queue.append(self.agent_id)
        self.agent_id+=1

    def exit(self):
        self.queue.serve()






b=Master()
b.enter()
b.enter()
b.enter()
b.exit()
b.enter()
b.enter()
b.exit()
b.exit()
b.enter()
print(b)


def main():
    pass


if __name__ == '__main__':
    main()
