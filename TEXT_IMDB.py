#import the required library to use
import pandas as pd

#just drag and drop the dataset file and it should be with extension csv
file = input('Enter full path of the data to process: ')
#order by the production year from new to old (descending)
df = pd.read_csv(file).sort_values(by='Year',ascending=False).reset_index(drop=True)

#working with the first 300 row of the dataset and columns of Title,Director,Rating
#df = pd.read_csv('C:\Data\Mohamed\Courses\ML\Python\Scripts\ipynb/IMDB-Movie-Data.csv').sort_values(by='Year',ascending=False).reset_index(drop=True)
df = df.loc[0:300][['Title','Director','Rating']]

#Making a 300*300 matrix with index of Director and columns of Title 
ratings_matrix = df.pivot_table(index='Director', columns='Title', values='Rating').fillna(0)
corr = ratings_matrix.corr()


#The user should enter the index number of favourite movie title of which he needs recommendation and prints the first 10 titles:
num1 = int(input('Enter index number of title: '))
res = pd.DataFrame(corr.iloc[num1])
res.columns = ['corr']
print(res.sort_values(by='corr',ascending=False).head(11).index[0:])

#Making a 300*300 matrix with index of Title and columns of Director(the tranpose of the first matrix)
ratings_matrix = ratings_matrix.T
corr = ratings_matrix.corr()


#The user should enter the index number of favourite movie director of which he needs recommendation and prints the first 10 directors:
num2 = int(input('Enter index number of director: '))
res = pd.DataFrame(corr.iloc[num2])
res.columns = ['corr']
print(res.sort_values(by='corr',ascending=False).head(11).index[0:])