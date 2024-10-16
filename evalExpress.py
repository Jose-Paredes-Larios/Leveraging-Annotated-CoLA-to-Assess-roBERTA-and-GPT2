import yaml
import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from src.utils.load_evaluations import load_evaluation
from src.utils.load_trainers import load_trainer
from src.utils.load_analysis import load_analysis

def generate_config_file(i):
    model_base_path = "/home/jparedeslarios/MidtermRep/robertaClassifiers/roberta"
    datafpath = "/home/jparedeslarios/MidtermRep/highArityEval.tsv"
    predfpath = f"/home/jparedeslarios/MidtermRep/highArityOutput{i}.tsv"
    model_path = f"{model_base_path}{i}"

    config_content = {
        'exp': 'TextClassification',
        'mode': ['evaluate'],
        'models': {
            'hf_text_classification_model': [model_path]
        },
        'id2label': {
            1: 'Positive',
            0: 'Negative'
        },
        'datafpath': datafpath,
        'predfpath': predfpath
    }

    config_filename = f"config_run_{i}.yaml"
    with open(config_filename, 'w') as config_file:
        yaml.dump(config_content, config_file)
    
    return config_filename

for i in range(1, 6):
    configfname = generate_config_file(i)
    sys.stderr.write(f'Reading from {configfname}\n')

    with open(configfname, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    modes = config['mode']
    for mode in modes:
        if mode == 'interact':
            exp = load_evaluation(config)
            exp.interact()
        elif mode == 'evaluate':
            exp = load_evaluation(config)
            exp.evaluate()
        elif mode == 'train':
            exp = load_trainer(config)
            exp.train()
        elif mode == 'analyze':
            exp = load_analysis(config)
            exp.analyze()
