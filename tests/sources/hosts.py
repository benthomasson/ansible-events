
def main(queue, args):

    for i in range(int(args['limit'])):
        queue.put(dict(i=i, meta=dict(hosts=['localhost0', 'localhost1'])))

if __name__ == "__main__":
    class MockQueue:
        def put(self, event):
            print(event)
    main(MockQueue(), dict(limit=5))



