class Queue():
    def __init__(self, queue_list):
        self.queue_list = queue_list

    def show_queue(self):
        return self.queue_list

    def is_queue_empty(self):
        return len(queue_list) == 0


    def put_element(self, item):
        self.queue_list.append(item)
        return self.queue_list

    def get_element(self):
        return self.queue_list.pop(0)


if __name__ == "__main__":
    queue_list = ["one element", "second element"]
    queue1 = Queue(queue_list)
    queue1.show_queue()

    print(queue1.is_queue_empty())

    item = "item1"
    queue1.put_element(item)

    queue1.get_element()