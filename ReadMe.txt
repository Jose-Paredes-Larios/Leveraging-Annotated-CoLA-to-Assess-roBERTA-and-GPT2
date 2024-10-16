Step 1: Training the Models

- First you must train five models. I have provided an example config file for training. All you have to do is put your desired model (don't change hf_text_classification_model:)

	- You may have noticed that I have also provided you with the train and valid tsv files. Thus, just change the "/home/jparedeslarios/MidtermRep/" part of the directories.

	- Also be sure to change the name of the model being saved (e.g. GPT2_a)

Step 2: Create the Evaluation Data Sets

- Here you are going to create a data set that your model can evaluate. To do so, open up the colaEval (base).xlsx file. Now just focus on columns D and beyond. Delete every column except the one containing the grammatical phenomenon you want to evaluate. For example, if I want to evaluate the model on "predicate", I would delete every column containing a grammatical phenomenon that is not "predicate". Make sure your grammatical phenomenon ends up at column D.

- Next go to the data tab in Excel. You'll notice a button that says sort. To the left of that button there is an arrow pointing down from Z to A. Select everything in column D and hit that Z to A button. Click sort on the pop-up. Every sentence that has a 1 in column D should be brought to the top. Delete every row that contains a 0 in column D; these sentences are towards the bottom because we sorted everything

- Now replace the grammatical phenomenon in cell 1D to condition (e.g. simple to condition).

- Now save as a tab delimited text (.txt). You can then change the extension to .tsv

	- I've run into some issues here where the .tsv file we made won't open in the toolkit. See if you can open it in the toolkit. If you can't and you are on Mac, open the file in numbers and export it as a .tsv file

- Lastly, I also provided an example of what the file you will evaluate should look like (predicateEval)

Step 3: Evaluate the Models 

- I have provided an example config file for evaluate. Once again, all you have to do is change the path to the model to one of the ones you created (e.g. gpt2_a). 
- datafpath should be directed to one of the files we created in step 2. 
- predfpath path will be where the output is stored. Note that the names should follow the following format: "[grammaticalPhenomenon]OuputX", where X is 1, 2, 3, 4, 5, ...
- Because we have five models, we will run evaluate five times to produce 5 different outputs. During each run, change the name of the output file in predfpath by incrementing the number, and the model you're using. 

Step 4: Obtaining MCC

- I have provided a python file called MCC.py. This will calculate the MCC of all 5 output files we created. All you have to do is change the directory in the MCC call done in main. 
- When putting in the directory leave out X.tsv. For example, if you have "/home/jparedeslarios/MidtermRep/argAltOutput1.tsv", you would put in "/home/jparedeslarios/MidtermRep/argAltOutput"
- Because of the way it is currently set up, make sure your output files are labeled 1 through 5. 

Congratulations! You are now an NLP Scholar B)
