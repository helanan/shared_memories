# shared_memories
Utilizing object serialization with python and pickling

Mary Margaret

In this exercise, you're going to use object serialization to allow two distinct Python modules pass a dictionary back and forth, while they are running independently of each other.

You will execute each module seperately, and each one will augment a dictionary, and then serialize it to a file.

Setup

mkdir -p ~/workspace/python/exercises/memories && cd $_
touch mary.py
touch margaret.py
Requirements

Create a mary.py module that contains a Mary class.
Create a margaret.py module that contains a Margaret class.
Each module must accept one command line argument that is a message to add to a list (see example below).
Each module must be able to serialize a dictionary to a file named messages.
Each module must be able to deserialize the dictionary stored in messages.
Each module, after the object is deserialized from the file, must add the message to the appropriate list in the dictionary.
Each module must handle exceptions properly. You may encounter the following while testing your logic.
FileNotFoundError
EOFError
KeyError
Tip: Make sure you import sys for the command line arguments, and pickle for serialization.
Dictionary structure

{
    "Mary": ["Hi, I'm Mary", "I like jet planes"],
    "Margaret": ["Hi, I'm Margaret", "I like cookies"]
}
Command line syntax

python mary.py "Hi, I'm Mary"
