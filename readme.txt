librarys required : Tensorflow,Pandas and Numpy
>> The objictive of this project is to identifies the crop map of given area with the help of Remote sensing data.
>> Landsat8 OLI Optical Remote sensing data was used in this project.
>> In the First step the Training Data sets are collected from known Pixel locations of diffrent crops.
>> crops are Paddy,Sugarcane,Chillies,Redgram,Cotton and Jowar.
>> For each crop 6 bands of Landsat8 data are used for the training (Blue,Green,Red,NIR,SWIR1,SWIR2)
>> In the second step Neural network was created with 6 input neurons and 6 output neurons 
>> Input Neurons are : Blue,Green,Red,NIR,SWIR1 and SWIR2.
>> Output Neurons are : Paddy,Sugarcane,Chillies,Redgram,Cotton and Jowar.
>> After the model is trained, the crop in the unknown pixals are identified.
