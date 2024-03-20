import pickle


def save(save_file_path, data):
    with open(save_file_path, 'wb') as f:
        pickle.dump(data, f)


def load(save_file_path):
    with open(save_file_path, 'rb') as f:
        return pickle.load(f)
