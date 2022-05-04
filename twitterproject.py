import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv(r'C:\Users\Abhishek Upadhyay\Documents\GitHub\Python\Resources\twitter.tsv', delimiter='\t')

dataset['id,label,tweet'][0]

import re
import nltk
from nltk.corpus import stopwords
from  nltk.stem.porter import PorterStemmer
ps=PorterStemmer()

dataset['id,label,tweet'][0]

clean_review=[]

for i in range(5000):
    text=re.sub('#[^a-zA-Z]',' ',dataset['id,label,tweet'][i])
    text=text.lower()
    text=text.split()
    text=[ps.stem(word) for word in text if not word in set(stopwords.words('english'))]
    #t1=ps.stem(word) for word in text  if not word in set (stopwords.words)
    text=' '.join(text)
    clean_review.append(text)
    
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=400)
X=cv.fit_transform(clean_review)
X=X.toarray()
y=dataset['id,label,tweet'].values

dataset['score'] = np.nan


dataset['id,label,tweet'] = np.nan
for i in range(5000):
    if( dataset['score'][i]>=3):
      dataset['label'][i]=1
    else:
       dataset['label'][i]=0
    


y=dataset['id,label,tweet'].values

############## Naive Bayes Algorithm ###############

from sklearn.naive_bayes import GaussianNB
nb=GaussianNB()
nb.fit(X,y)
nb.score(X,y)

############# Logistic Regression #################

from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X,y)
log_reg.score(X,y)

############ KNN #########################


from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier()
knn.fit(X,y)
knn.score(X,y)

############ Decision Tree Classifier #############

from sklearn.tree import DecisionTreeClassifier
dtf=DecisionTreeClassifier()
dtf.fit(X,y)
dtf.score(X,y)


############ SVM ################################

from sklearn.svm import SVC
svm=SVC()
svm.fit(X,y)
svm.score(X,y)

############# Printing all the relevant features for classification ############

print(cv.get_feature_names())   










#from sklearn.naive_bayes import GaussianNB
#nb=GaussianNB()
#nb.fit(X,y)

#nb.score(X,y)
    
    

