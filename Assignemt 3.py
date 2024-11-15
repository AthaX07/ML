import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
plt.style.use("fivethirtyeight")

df = pd.read_csv("/home/avcoe/Admission_Predict.csv")
df.head()

#information of the dataset used in the practical
df.info()

  
# dataframe.size
size = df.size
print("Size of dataset is :",size)
  
# dataframe.shape
shape = df.shape
print("shape of datset is \n\n:",shape)

print(df.describe())

print(df.head())

#Data type of each column
print("Data Type for Each Columns are\n",df.dtypes.value_counts())

df.dtypes == 'object'

n = df.columns[df.dtypes != 'object']

#display all values
df[n]

#display missing values
print("",df[n].isnull())

#All zeros
df[n].isnull().sum().sort_values(ascending=False)

#finding % of missing values in each column
df[n].isnull().sum().sort_values(ascending=False)/len(df)

dataset = df

from sklearn.preprocessing import StandardScaler

s_sc = StandardScaler()
col_to_scale = ['GRE Score', 'CGPA']
dataset[col_to_scale] = s_sc.fit_transform(dataset[col_to_scale])


#Spliting the data into training and testing data
from sklearn.model_selection import train_test_split

X = dataset.drop('target', axis=1)
y = dataset.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#Classification using Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier

tree_clf = DecisionTreeClassifier(random_state=42)
tree_clf.fit(X_train, y_train)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def print_score(clf, X_train, y_train, X_test, y_test, train=True):
    if train:
        pred = clf.predict(X_train)
        clf_report = pd.DataFrame(classification_report(y_train, pred, output_dict=True))
        print("Train Result:\n================================================")
        print(f"Accuracy Score: {accuracy_score(y_train, pred) * 100:.2f}%")
        print("_______________________________________________")
        print(f"CLASSIFICATION REPORT:\n{clf_report}")
        print("_______________________________________________")
        print(f"Confusion Matrix: \n {confusion_matrix(y_train, pred)}\n")
        
    elif train==False:
        pred = clf.predict(X_test)
        clf_report = pd.DataFrame(classification_report(y_test, pred, output_dict=True))
        print("Test Result:\n================================================")        
        print(f"Accuracy Score: {accuracy_score(y_test, pred) * 100:.2f}%")
        print("_______________________________________________")
        print(f"CLASSIFICATION REPORT:\n{clf_report}")
        print("_______________________________________________")
        print(f"Confusion Matrix: \n {confusion_matrix(y_test, pred)}\n")

print_score(tree_clf, X_train, y_train, X_test, y_test, train=True)
print_score(tree_clf, X_train, y_train, X_test, y_test, train=False)

print(accuracy_score(y_train, tree_clf.predict(X_train)) * 100)
print(accuracy_score(y_test, tree_clf.predict(X_test)) * 100)



