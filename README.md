# masseyhacksv



## Inspiration
Our drive and curiousity for machine learning, cyber security, and data science pushed us to make a complex antivirus with intruistic features beyond our years of experience by simply collaborating together and using the opportunity our parents gave us to make the best of ourselves.

## What it does
TechSavvyGranny is machine-learning oriented. Essentially, the software checks files as they are downloaded. If a file is flagged as malicious, it can then be targeted for further examination or eliminated. The most important part of this software is the methods used to obtain an accurate machine learning model. We parsed PE file headers because they conceal a large amount of data about an executable file. 

## How we built it
Our antivirus was written mainly in python3 and is driven by supervised machine learning. We used Keras, and NumPy to supervise the AI. As an additional feature we used the classic signature method to help increase overall malware detection for our program. We used a dataset with PE (Portable Executable) file headers to train our model to recognize malicious patterns. We also set up multiple monitoring systems for packet analysis, and RAM usage. We used data normalization to increase accuracy and learning speed for the AI.

## Challenges we ran into
One of the main challenges we ran into was formatting the .csv dataset the right way for the AI to start progressing properly. Our dataset was extremely big and wasn't formatted in the most efficient way that slowed our learning speed by hours.

## Accomplishments that we're proud of
- Having a full working AI model with 80% accuracy for malware detection
- Successfully learning how to use Keras, and Tensorflow library
- In-Depth profiency for detection of different malware features.
- Creating such a complex project in 24 hours
- Being completely sleep deprived for the whole competition 

## What we learned
- How to successfully implement machine learning libraries 
- Learned how to use supervised machine learning for malware detection
- How to normalize data
- Learned to use the Google Cloud Platform for AI development 
- Python3

## What's next for TechSavvyGranny
We hope to bring TechSavvyGranny to the people who need its services most.
