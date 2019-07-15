# precision, recall, f1-score report
from sklearn.metrics import classification_report
print(classification_report(np.concatenate(y_true), np.concatenate(y_pred)))


# split train, valid set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)