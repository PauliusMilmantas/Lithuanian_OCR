import os
import shutil

training_perc = 0.7
testing_perc = 0.1
validation_perc = 0.2

classes = os.listdir('data/')

idx_test = 0
idx_val = 0
idx_train = 0
for cls in classes:

    if(os.path.isdir('training/' + cls) == False):
        os.mkdir('training/' + cls)

    if(os.path.isdir('test/' + cls) == False):
        os.mkdir('test/' + cls)

    if(os.path.isdir('val/' + cls) == False):
        os.mkdir('val/' + cls)

    files = os.listdir('data/' + str(cls) + '/')

    amount_to_train = int(len(files)*training_perc)
    amount_to_test = int(len(files)*testing_perc)
    amount_to_validate = len(files) - amount_to_test - amount_to_train

    for i in range(len(files)):
        if(amount_to_train != 0):
            amount_to_train -= 1
            shutil.move('data/' + cls + '/' + files[i], 'training/' + cls + '/' + str(idx_train) + '.jpg')

            idx_train += 1
        elif(amount_to_test != 0):
            amount_to_test -= 1
            shutil.move('data/' + cls + '/' + files[i], 'test/' + cls + '/' + str(idx_test) + '.jpg')

            idx_test += 1
        else:
            amount_to_validate -= 1
            shutil.move('data/' + cls + '/' + files[i], 'val/' + cls + '/' + str(idx_val) + '.jpg')

            idx_val += 1
