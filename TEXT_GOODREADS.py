#import the required library to use
import pandas as pd

#just drag and drop the dataset file and it should be with extension csv
file = input('Enter full path of the data to process: ')
#order by the average rating from high to low (descending)
df = pd.read_csv(file).sort_values(by='average_rating',ascending=False).reset_index(drop=True)

#working with the first 300 row of the dataset and columns of title,authors,average_rating
#df = pd.read_csv('C:\Data\Mohamed\Courses\ML\Python\Scripts\ipynb/books.csv')
df = df.loc[0:300][['title','authors','average_rating']]

#Making a 300*300 matrix with index of authors and columns of title 
ratings_matrix = df.pivot_table(index='authors', columns='title', values='average_rating').fillna(0)
corr = ratings_matrix.corr()


#The user should enter the index number of favourite book title of which he needs recommendation and prints the first 10 titles:
num1 = int(input('Enter index number of title: '))
res = pd.DataFrame(corr.iloc[num1])
res.columns = ['corr']
print(res.sort_values(by='corr',ascending=False).head(11).index[0:])

#Making a 300*300 matrix with index of title and columns of authors(the tranpose of the first matrix)
ratings_matrix = ratings_matrix.T
corr = ratings_matrix.corr()


#The user should enter the index number of favourite book author of which he needs recommendation and prints the first 10 authors:
num2 = int(input('Enter index number of author: '))
res = pd.DataFrame(corr.iloc[num2])
res.columns = ['corr']
print(res.sort_values(by='corr',ascending=False).head(11).index[0:])