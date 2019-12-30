# kNN-Diabetes
Model for classifying test objects in two classes - has diabetes and no diabetes

There are two versions of the model:

  - One using euclidian (Knn-euc.py)
  - One using cosine similarity (Knn-cos.py) (
This report used the cosine proximity measure)

### Understanding the model and the dataset
  1. Introduction
  2. Development
  3. Conclusion

### 1- Introduction
In this work we used the database “Pima Indians Diabetes Database” to
apply the concepts learned in the classroom, such as data processing techniques,
proximity and classification algorithms. Its purpose is to train an algorithm with
training objects so that it can classify new test objects into two classes
distinct: people with diabetes and people without diabetes.

The database used has 768 objects, representing women with at least
21 years of age, 500 of them are objects of class 0 (do not have diabetes) and 268 are of the
class 1 (have diabetes), in addition the attributes of this database are:

    1. Number of times you became pregnant (Standard deviation: 3.4)
    2. 2-hour plasma glucose concentration in an oral glucose tolerance test (Standard deviation: 32.0)
    3. Diastolic blood pressure (Standard deviation: 19.4)
    4. Triceps skinfold thickness (Standard deviation: 16.0)
    5. 2 hour serum insulin (Standard deviation: 115.2)
    6. Body mass index (Standard deviation: 7.9)
    7. Diabetes pedigree function (Standard deviation: 0.3)
    8. Age in years (Standard deviation: 11.8)

To perform this task of classifying objects, the following techniques were used:

- Data processing method: Min-max
- Proximity Measure: Cosine Similarity
- Classification algorithm: k Nearest Neighbors (kNN)

By analyzing the standard deviation of each attribute we can see that there is a huge
discrepancy between their values. This fact is one of the reasons for using the method
min-max for data processing because it transforms all database values
in a new value between 0 and 1. Another reason for using this type of method is
use a scale where the proximity value indicates the similarity / dissimilarity fraction
between two objects.

After all values ​​are on a scale between zero and one, the next step is to apply
the k-NN algorithm, that is, for each new test object, we must calculate the measure of
proximity between it and all the training objects and then sort by increasing or
decreasing (according to the measure used) and analyze the class of the first k objects. The
test object class will be defined from the most predominant class among these first k
objects.

The way we are going to order the proximity measurements depends on the same as it was
chosen. Basically we sort of ascending as we choose
explains how two objects are different, that is, the smaller the value obtained, the more
objects are similar (they are close). Analogously we order the measures so
decreasing when the measure we choose spells out how much two objects are equal, ie
the higher the value obtained, the more similar the objects are. These two methods portray the
similarity and dissimilarity, respectively.

### 2 - Development
Two tests were performed with the program, one with the value of k equal to 3 and the other with k
equal to 7. In the first test (k == 3) the algorithm correctly classified 124 objects, obtaining
64.58% accuracy and its confusion matrix was organized as follows:

- True Positives: 30
- True Negatives: 94
- False Positives: 27
- False Negatives: 41
- Sensitivity: 42.25%
- Specificity: 77.69%

In the second test (k == 7) the algorithm correctly classified 119 objects, obtaining
61.98% accuracy and its confusion matrix was organized as follows:

- True Positives: 23
- True Negatives: 96
- False Positives: 25
- False Negatives: 48
- Sensitivity: 32.39%
- Specificity: 79.34%

Based on the results of the two tests we can say that the first one got better
results, because its accuracy was higher and mainly its Sensitivity was also higher.
Among all performance and efficiency measures, we are primarily interested in
Sensitivity as possible, because for this particular database, our main
The objective is to identify who are the people who have diabetes, ie the "positive" class.
Knowing this, High Sensitivity is the most desired performance measure because your result
demonstrates that 42.25% of all people who actually had
diabetes.

The best choice of parameter "k" depends on the data we are using, on average
the higher the k value, the greater the reduction in the negative effect that noise causes on
classification but on the other hand it can relate the test object to other training objects that
they are relatively distant in terms of the proximity measure chosen.
Let's look at a third test, this time with k equal to 81:

The algorithm correctly classified 127 objects with an accuracy of 66.15%, obtaining the
following matrix of confusion:

- True Positives: 20
- True Negatives: 107
- False Positives: 14
- False Negatives: 51
- Sensitivity: 28.17%
- Specificity: 88.43%

Analyzing the results of the third test with the other two we can see that the
accuracy for k equal to 81 is higher than for values ​​3 and 7. But despite obtaining the highest
accuracy, this test obtained the lowest Sensitivity, that is, this algorithm classified
erroneously 71.83% of all people who had diabetes. In terms of utility
(correctly identify people with diabetes), the k test of 81 obtained the
worse performance compared to others.

Another factor that directly impacts the test result is the proximity measurement.
used, in this case we are using a measure that is not recommended to solve the type
problem that our chosen database addresses. The similarity of the cosine is very
used to analyze documents and make them look alike even though
Very different size.

In general, the more training objects we have and we can eliminate the more
The more noise, the better the k-NN algorithm results. However, in the case of this
data we are analyzing, choose another measure of proximity (such as the
Euclidean distance or that of Manhattan) would be an option that will most likely influence
in a more efficient classification algorithm, that is, that classifies the test objects of
most accurate way. cosine similarity is not the most appropriate measure for
solve the kind of problem we are dealing with.

### 3 - Conclusion
All the results we got from the tests done in topic 2, in terms of
accuracy, sensitivity and specificity are totally dependent on the proximity measure
that we use. Cosine similarity is a measure of proximity that makes explicit the
similarity between two objects. More specifically, cosine similarity measures
cosine of the angle between two vectors projected in a multidimensional space. The main
functionality of this measure is to determine how two documents look alike regardless
of their sizes.

This measure is widely used, and is also quite efficient for spam detection. THE
from parsing words that typically characterize an email class that is not
relevant to a user (the concept of spam is different for each type of user, taking into
interests), the algorithm that uses cosine similarity can
classify new emails very accurately by classifying them as spam and not spam.

However, by applying such proximity measure in the classification of diabetic and non-diabetic people
cosine similarity did not perform well because its accuracy and
mainly its sensitivity in this application are not at a desirable value for a
possible application that would be used in real life.

The explanation for this measure not performing well in our database is
because it deals with data that have different characteristics from the other bases that the
cosine similarity is indicated. The relationship between the attributes is different as well as the
classification (quantitative and qualitative), variance, and various other factors. This question of
data type incompatibility with the proximity measure used could be
resolved if specific preprocessing was performed to change properties of the
data in our database in order to improve the performance of cosine similarity.

So the main improvement our algorithm could have to better classify the
test objects would be to alter the proximity measure used, since the similarity of the cosine
It is not intended to solve the type of problem we are using. In addition our base
of data has a specific characteristic that makes the classification itself difficult:
attributes have very discrepant values, while one has a standard deviation of 0.3 (att
number 7), another has a standard deviation of 115.2 (att number 5).
