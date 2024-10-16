import pandas as pd
import csv
import math

def ensemble(fname: str, outputF: str, evalF:str):
    input_files = ['1','2','3','4','5']
    for i in range (0,5):
        input_files[i]=fname+str(i+1)+".tsv"
        
    output_data = {f'output {i+1}': [] for i in range(5)}

    for i, file in enumerate(input_files):
        df = pd.read_csv(file, sep='\t') 
    
        for predicted in df['predicted']:
            if predicted == 'Negative':
                output_data[f'output {i+1}'].append(0)
            else:
                output_data[f'output {i+1}'].append(1)
    
    output_df = pd.DataFrame(output_data)
    output_df.to_csv(outputF, sep='\t', index=False)
    
    df = pd.read_csv(outputF, sep='\t')
    df['predicted'] = df[['output 1', 'output 2', 'output 3', 'output 4', 'output 5']].mode(axis=1)[0]
    df['predicted'] = df['predicted'].map({1: 'Positive', 0: 'Negative'})

    eval_df = pd.read_csv(evalF, sep='\t')
    df['target'] = eval_df['target']
    
    df.to_csv(outputF, sep='\t', index=False)

def main():
    ensemble("/home/jparedeslarios/MidtermRep/major/argAlt/argAltOutput", "/home/jparedeslarios/MidtermRep/argAltMajority.tsv", "/home/jparedeslarios/MidtermRep/major/argAlt/argAltEval.tsv")

if __name__ == '__main__':
    main()