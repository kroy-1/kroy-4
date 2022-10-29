# importing pandas as pd for using data frame

import pandas as pd

 

# creating dataframe with student details

dataframe = pd.DataFrame({'id': [7058, 4511, 7014, 7033],

                          'name': ['sravan', 'manoj', 'aditya', 'bhanu'],

                          'Maths_marks': [99, 97, 88, 90],

                          'Chemistry_marks': [89, 99, 99, 90],

                          'telugu_marks': [99, 97, 88, 80],

                          'hindi_marks': [99, 97, 56, 67],

                          'social_marks': [79, 97, 78, 90], })

 

# display dataframe

dataframe
