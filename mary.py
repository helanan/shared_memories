import pickle


class Messages:

    def __init__(self):
        self.all_messages = []
        try:
            self.all_messages = self.deserialize()
        except FileNotFoundError:
            pass

    def list_messages(self):
        for key, message in enumerate(self.all_messages):
            print(str(key) + ": " + message)

    def prompt(self):
        message = input("Hi, Im Mary...")

        if message == "ls":
            self.list_messages()

        elif message == "rm":
            self.list_messages()
            deleted = input("Which one?")
            del(self.all_messages[int(deleted)])

        elif message != "quit":
            self.all_messages.append(message)
            self.serialize()

        if message != "quit": self.prompt()

    def serialize(self):
        with open(messages.txt, wb+) as message_text:
            pickle.dump(self.all_messages, message_text)

    def deserialize(self):
        try:
            with open(messages.txt, rb+) as message_text:
                self.all_messages = pickle.load(message_text)
        except EOFError:
            pass

        return self.all_notes
