import numpy as np

def preprocess_input(total_sqft,bath,balcony,bhk,location,columns):

    x = np.zeros(len(columns))

    x[0] = total_sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk

    try:
        loc_index = columns.index(f'location_{location}')
        x[loc_index] = 1
    except:
        pass

    return x