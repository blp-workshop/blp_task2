# Task 2: Sentiment Analysis

The aim of this task is to identify the polarity of social media content. This year, we offer only one subtask. Please see the 
[Task Description](#task-description) below.


__Table of contents:__
- [List of Versions](#list-of-versions)
- [Contents of the Directory](#contents-of-the-directory)
- [Task Description](#task-description)
- [Dataset](#dataset)
- [Scorer and Official Evaluation Metrics](#scorer-and-official-evaluation-metrics)
- [Baselines](#baselines)
- [Format checker](#formatchecker)
- [Submission Guidelines](#submission-guidelines)
- [Licensing](#licensing)
- [Credits](#Credits)

## List of Versions
* __[13/07/2023]__  Training and dev data released for both subtask



## Contents of the Directory
* Main folder: [data](./data)<br/>
  This directory contains files for the subtasks.
* Main folder: [baselines](./baselines)<br/>
	Contains scripts provided for baseline models of the tasks.
* Main folder: [format_checker](./format_checker)<br/>
	Contains scripts provided to check the format of the submission file.
* Main folder: [scorer](./scorer)<br/>
	Contains scripts provided to score the output of the model when provided with the label (i.e., dev).

* [README.md](./README.md) <br/>
	This file!

## Task Description

**Task 2:** Given a text, detect the fine-grained positive class, if any. This is a multiclass classification task. The fine-grained labels include _Positive_, _Negative_, Neutral


## Dataset

### Input data format
Each file uses the tsv format. A row within the tsv adheres to the following structure:
```
id	text	label
```
Where:
* id: sentence id for a given political debate
* text: sentence's text
* label: Positive, Negative, or Neutral
* 
##### Example
```
14737	এখান থেকে সবাই শিক্ষা নিতে পারি ।	Positive
```

## Scorer and Official Evaluation Metrics

### Scorers

The scorer for the task 2 is located in the [scorer](scorer) module of the project. The scorer will report official evaluation metrics and other metrics of a prediction file. The scorer invokes the format checker for the task to verify the output is properly shaped.
It also handles checking if the provided predictions file contains all tweets from the gold one.


You can install all prerequisites through,
```
pip install -r requirements.txt
```
Launch the scorer for the task 2 as follows:
```
python scorer/task2.py --gold-file-path=<path_gold_file> --pred-file-path=<predictions_file>
```


##### Example

```
python scorer/task2.py --pred_files_path task2_dev_output.txt --gold_file_path data/dev.tsv
```

### Official Evaluation Metrics
The **official evaluation metric** for the task is **macro-F1**. However, the scorer also reports accuracy, precision and recall.


## Baselines

The [baselines](baselines) module currently contains a majority, random and a simple n-gram baseline for Task 2. 

Baseline Results for Task 2 on Dev-Test set

| Model                      | macro-F1 |
|----------------------------|----------|
| Random Baseline            | 0.3244   |
| Majority Baseline          | 0.2210   |
| n-gram Baseline            | 0.4436   |

## Format checker

The format checkers for both subtasks are located in the [format_checker](format_checker) module of the project. The format checker verifies that your generated results file complies with the expected format.

Before running the format checker please install all prerequisites,
```
pip install -r requirements.txt
```

To launch it, please run the following command:

```
python format_checker/task2.py -p paths_to_your_results_files
```

##### Example
```
python format_checker/task2.py -p ./task2.txt
```
**paths_to_your_results_files**: can be one path or space-separated list of paths


**Note that the checker cannot verify whether the prediction file you submit contains all lines, because it does not have access to the corresponding gold file.**


## Submission

### Guidelines

The process consists of two phases:

1. **System Development Phase:** This phase involves working on the *dev-test set*.
2. **Final Evaluation Phase:** This phase involves working on the *test set*, which will be released during the ***evaluation cycle***.
For each phase, please adhere to the following guidelines:

- Each team should create and maintain a single account for submissions. Please ensure all runs are submitted through this account. Submissions from multiple accounts by the same team could result in your system being not ranked in the overview paper.
- The most recent file submitted to the leaderboard will be considered your final submission.
- The output file must be named task2.tsv. Failure to follow this naming convention will result in an error on the leaderboard.
- You are required to compress the .tsv file into a .zip file (for example, zip task2.zip task2.tsv) and submit it via the Codalab page.
- Please include your team name and a description of your method with each submission.
- You are permitted to submit a maximum of 200 submissions per day for the Task.


### Submission Site
**TBA**


## Licensing
The dataset is free for general research use.


## Credits
- Md. Arid Hasan, GRA, University of New Brunswick
- Shudipta Das, Daffodil International University
- Afiyat Anjum, Daffodil International University
- Anika Anjum, Daffodil International University
- Dr. Firoj Alam, Scientist, Qatar Computing Research Institute
- [SentiNOB](https://aclanthology.org/2021.findings-emnlp.278.pdf)