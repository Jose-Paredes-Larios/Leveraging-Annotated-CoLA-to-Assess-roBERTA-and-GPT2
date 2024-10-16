import csv
import math

def MCC(fname: str) -> float:
    true_negative = 0.0
    true_positive = 0.0
    false_positive = 0.0
    false_negative = 0.0

    with open(fname, newline='') as data:
        reader = csv.DictReader(data, delimiter='\t')
    
        for row in reader:
            # Access values in the 'target' and 'predicted' columns for the current row
            target = int(row['target'])        # Get target value for the current row
            predicted = (row['predicted'])  # Get predicted value for the current row
        
            # True Negative
            if target == 0 and predicted == "Negative":
                true_negative += 1
        
            # True Positive
            elif target == 1 and predicted == "Positive":
                true_positive += 1
        
            # False Positive
            elif target == 0 and predicted == "Positive":
                false_positive += 1
        
            # False Negative
            elif target == 1 and predicted == "Negative":
                false_negative += 1

    #print(f"True Negatives: {true_negative}")
    #print(f"True Positives: {true_positive}")
    #print(f"False Positives: {false_positive}")
    #print(f"False Negatives: {false_negative}")

    return ((true_positive * true_negative) - (false_positive * false_negative))/(math.sqrt((true_positive+false_positive)*(true_positive+false_negative)*(true_negative+false_positive)*(true_negative+false_negative)))




def main():
    for i in range(1,6):
            print("This is MCC "+str(i)+": "+str(MCC("/home/jparedeslarios/MidtermRep/argAltOutput"+str(i)+".tsv")))

if __name__ == '__main__':
    main()