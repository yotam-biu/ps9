# tutorial9

## 1. **Load the dataset:**  

   After running the first cell of this notebook, the file `parkinson.csv` will appear in the `Files` folder.
   You need to loaded the file as a DataFrame.  

## 2. **Select features:**  

   - Choose **two features** as inputs for the model.  
   - Identify **one feature** to use as the output for the model.  

  #### Advice:  
  - You can refer to the paper available in the GitHub repository for insights into the dataset and guidance on identifying key features for the input and output.  
  - Alternatively, consider creating pair plots or using other EDA methods we learned in the last lecture to explore the relationships between features and determine which ones are most relevant.

## 3. **Scale the data:**

   Apply the `MinMaxScaler` to scale the two input columns to a range between 0 and 1. 

## 4. **Split the data:**

   Divide the dataset into a training set and a validation set.

## 5. **Choose a model:**  

   Select a model to train on the data.  

   #### Advice:  
   - Consider using the model discussed in the paper from the GitHub repository as a reference.  

# 6. **Test the accuracy:**  

   Evaluate the model's accuracy on the test set. Ensure that the accuracy is at least **0.8**.  

## 7. **Save and upload the model:**  

   After you are happy with your results, save the model with the `.joblib` extension and upload it to your GitHub repository main folder.
   
   Additionally, update the `config.yaml` file with the list of selected features and the model's joblib file name.  


example:  
```yaml
selected_features: ["A", "B"]  
path: "my_model.joblib"
```

## 8. **Copy the code:**  

   Copy and paste all the code from this notebook into a `main.py` file in the GitHub repository.  

