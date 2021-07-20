import sys

def get_character_frequency(data):
    ##returns dictionary of character counts
    


def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


    ##create huffman encoding and test it works by comparison to encoded strings for some basic words

    ##store the nodes themselves in the qeueue, which will reference their children.

    ##call get_char_freq to get character counts, the loop over it to create node and store each node in list

    ##then sort the list

    ##then begin building the tree, where highest priority (loweste freq) popped out first, their values from their nodes added, and new node (without letter property)
    ##with left and right child properties set