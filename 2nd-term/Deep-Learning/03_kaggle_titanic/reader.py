import numpy as np
import csv

class reader(object):
    def __init__(self, data_file="./data/train.csv", val_size=100):
        # Store header and value separately.
        self.value = []
        with open(data_file, 'r') as f:
            data = csv.reader(f, delimiter=',')
            for i, row in enumerate(data):
                if i == 0:
                    self.attribute = row
                    continue
                self.value.append(row)

        # Change type from list to ndarray.
        self.raw_to_vector(self.value)
        # split data into train, validation set.(x, y, id)
        self.train_validation_split(val_size)

        self.start_index_train = 0
        self.start_index_val = 0

        self.shuffled_indices_train = list(range(self.train_size))
        self.shuffled_indices_val = list(range(self.val_size))

    def raw_to_vector(self, value):
        self.x = []
        self.y = []
        self.id = []
        for row in self.value:
            x = [0] * 6

            # PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
            x[0] = float(row[2]) # Pclass
            x[1] = 0 if row[4] == 'male' else 1 # Sex; male 1, femail 2
            try:
                x[2] = float(row[5]) # Age
            except:
                x[2] = 20.0
            x[3] = float(row[6]) # SibSp
            x[4] = float(row[7]) # Parch
            x[5] = float(row[9]) # Fare

            self.id.append(int(row[0])) # Survived
            self.y.append(int(row[1])) # Passenger ID
            self.x.append(x)

        self.x, self.y, self.id = np.array(self.x), np.array(self.y), np.array(self.id)

    def next_batch(self, batch_size, x_type='train'):
        if x_type == 'train':
            if self.start_index_train == 0:
                np.random.shuffle(self.shuffled_indices_train)

            end_index = min([self.train_size, self.start_index_train + batch_size])
            batch_indices = [self.shuffled_indices_train[idx] \
                             for idx in range(self.start_index_train, end_index)]

            batch_x = self.x_train[batch_indices]
            batch_y = self.y_train[batch_indices]
            batch_id = self.id_train[batch_indices]

            if end_index == self.train_size:
                self.start_index_train = 0
            else:
                self.start_index_train = end_index
        else:
            if self.start_index_val == 0:
                np.random.shuffle(self.shuffled_indices_val)

            end_index = min([self.val_size, self.start_index_val + batch_size])
            batch_indices = [self.shuffled_indices_val[idx] \
                             for idx in range(self.start_index_val, end_index)]

            batch_x = self.x_val[batch_indices]
            batch_y = self.y_val[batch_indices]
            batch_id = self.id_val[batch_indices]

        return batch_x, batch_y, batch_id

    def train_validation_split(self, val_size):
        self.x_train = self.x[:-val_size]
        self.x_val = self.x[-val_size:]

        self.y_train = self.y[:-val_size]
        self.y_val = self.y[-val_size:]

        self.id_train = self.id[:-val_size]
        self.id_val = self.id[-val_size:]

        self.val_size = val_size
        self.train_size = len(self.x_train)
