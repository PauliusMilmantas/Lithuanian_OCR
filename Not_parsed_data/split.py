import os
import shutil

training_perc = 0.7
testing_perc = 0.1
validation_perc = 0.2

classes = os.listdir('data/')
for cls in classes:

    idx = 0

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
            shutil.move('data/' + cls + '/' + files[i], 'training/' + cls + '/' + str(idx) + '.jpg')

            if(amount_to_train == 0):
                idx = -1
        elif(amount_to_test != 0):
            amount_to_test -= 1
            shutil.move('data/' + cls + '/' + files[i], 'test/' + cls + '/' + str(idx) + '.jpg')

            if(amount_to_test == 0):
                idx = -1
        else:
            amount_to_validate -= 1
            shutil.move('data/' + cls + '/' + files[i], 'val/' + cls + '/' + str(idx) + '.jpg')

        idx += 1
