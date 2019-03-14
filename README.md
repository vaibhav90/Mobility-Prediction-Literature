# Literature on human mobility modeling and prediction


#### The metadata is collected from the following indexing bodies  
  - ##### [Web of Science](https://apps.webofknowledge.com/WOS_GeneralSearch_input.do?product=WOS&search_mode=GeneralSearch&SID=C5uHbS2XkmFRw4V47rb&preferencesSaved=)
  - ##### [Microsoft Academic Search](https://preview.academic.microsoft.com/home)
  - ##### [Semantic Scholar](https://www.semanticscholar.org/)

##### The scrapping from Semantic Scholar is done using [https://open.semanticscholar.org/](https://api.semanticscholar.org/)
##### The scrapping was done using the following Keywords and restricted to these domains [Computer science, Computer network, Mobility model, Distributed computing, Real-time computing, Wireless ad hoc network, Handover, Artificial intelligence, Optimized Link State Routing Protocol, Machine learning, Quality of service, Wireless Routing Protocol, Data mining, KDD, Wireless network, Mobile ad hoc network, Ad hoc wireless distribution service, Mobile computing, Mobility management, Adaptive quality of service multi-hop routing]
- ##### Human-mobility prediction
- ##### Human-mobility modeling
- ##### Next place forecasting
- ##### Next place prediction
- ##### Predicting User Movement
- ##### Predicting Significant locations
- ##### Predicting User Movement

##### The metadata is in the following format
##### Paper Title | Publication Year | Publication Venue | Authors | Keyword List
![alt text](https://github.com/vaibhav90/Mobility-Prediction-Literature/blob/master/images/met_data.jpg)


##### The pipeline for cleaning the collected data is described below
![alt text](https://github.com/vaibhav90/Mobility-Prediction-Literature/blob/master/images/scrapping.png)

##### The string similarity and profiling was performed using [python-string-similarity](https://github.com/luozhouyang/python-string-similarity)

##### The raw_data folder contains raw data scrapped from all the platforms with the title indicating the key word searched for

##### The scripts folder contains python scripts used to scrape, preprocess, clean and merge the data collected from different sources.

##### The file literature_metadata contains the merged list and literature_with_abstracts contains all the abstracts
