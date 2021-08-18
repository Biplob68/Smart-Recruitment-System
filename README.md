                                                     Smart Recruitment System
#### _A Django-based resume ranker website where recruiter can post jobs, candidate can apply for the job, fill in the required data, upload resumes, and the system shortlists the candidate resumes. The system ranks the CVs based on the document similarity of the job description and the resumes using the KNN model and shows the shortlist._

## _Introduction:_
_Find the best candidate from a recruitment process within the shortest time is challenging for a company. For this purpose, we proposed a recruitment system where recruiters will post their current vacancy with some personality questions. Then applicants will answer all the questions along with dropping the CV for a particular job. Then, the system will automatically parse the resume to find out the required skills and produce a shortlist by combining question answering and resume parsing score._

## _Objective:_
* Find the best candidates.
* Provide a more realistic ranking system.
* Make the recruiting process more flexible.
* Save human efforts, time, and cost.

## _System Architecture:_
![system architecture (1)](https://user-images.githubusercontent.com/66861180/129874802-22818723-4102-46a8-a44e-aaab377281d5.png)

## _Ranking Model:_
![Model architecture](https://user-images.githubusercontent.com/66861180/129875039-633c9bbf-0e5b-4552-8352-c145c961ef2c.png)
* **Data Cleaning:** The system cleans the special characters, signals, and numbers from the extracted data.
* **Tokenization:** The clean extracted data are converted into tokens.
* **Data Preparation:** Stops words are removed and the tokens are stemmed.
* **Requirement Extraction:** The relevancy of important words is extracted using TF-IDF from each CV data and mapped to the CV based on the given requirements.
* **Matching Similarity:** The system collects the CVs that are more compatible with thevacancy based on the required skills.
* **Ranking:** After matching similarity, the system will generate a rank that will show the topk’s CVs. For example: top 20 CVs.
* **Final result:** Next the final result will be calculated based on the score from assessments and matching skillset.




## _Design Algorithm:_
* **Basic Requirements:** Academic CGPA or degree, experience year.
* **Data Pre-processing:** Data cleaning, Word Stemming, Verb Lemmatizing.
* **Calculate TF-IDF:** 
   * _TF(‘keyword’) = number of appeared (‘keyword’) / Total number of (‘keyword’)_
   * _IDF(‘keyword’) = log(total number of resume / total number of the resume with term ‘keywords’). It sets IDF log value = 1 for the required resume and 0 for the unwanted._
   * _weight(‘keyword’) = TF(‘keyword’) * IDF(‘keyword’)_
   
* **Document Similarity Matching Score:** TF-IDF weight, KNN.
* **Final Score**.
   
