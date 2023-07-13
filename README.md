# Sentiment Analysis Shared Task at [BLP Workshop @ EMNLP 2023](https://blp-workshop.github.io/)

The aim of this task is to identify the polarity of social media content. Please see the
[Task Description](#task-description) below.


__Table of contents:__
- [Important Dates](#important-dates)
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

## Important Dates
- **15 July 2023:** Registration on codalab and beginning of the development cycle
- **20 August 2023:** Beginning of the evaluation cycle (test sets release and run submission)
- **25 August 2023:** End of the evaluation cycle
- **1 September 2023:** Paper submission due
- **29 September 2023:** Notification of acceptance
- **6 October 2023:** Camera-ready due
- **7 December 2023:** Workshop co-located with EMNLP (Singapore)

## Recent Updates
* __[13/07/2023]__  Training and dev data released



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

**Task:** The objective is to detect the sentiment associated within a given text. This is a multi-class classification task that involves determining whether the sentiment expressed in the text is _Positive_, _Negative_, _Neutral_.

## Dataset

### Input data format
Each file uses the tsv format. A row within the tsv adheres to the following structure:

```
id	text	label
```
Where:
* id: an index or id of the text
* text: text
* label: Positive, Negative, or Neutral

##### Example
```
14737	এখান থেকে সবাই শিক্ষা নিতে পারি ।	Positive
```

## Scorer and Official Evaluation Metrics

### Scorers

The scorer for the task is located in the [scorer](scorer) module of the project. The scorer will report official evaluation metrics and other metrics of a prediction file. The scorer invokes the format checker for the task to verify the output is properly shaped.
It also handles checking if the provided predictions file contains all tweets from the gold one.


You can install all prerequisites through,
```
pip install -r requirements.txt
```
Launch the scorer for the task as follows:
```
python scorer/task.py --gold-file-path=<path_gold_file> --pred-file-path=<predictions_file>
```


##### Example

```
python scorer/task.py --pred_files_path task_dev_output.txt --gold_file_path data/dev.tsv
```

### Official Evaluation Metrics
The **official evaluation metric** for the task is **micro-F1**. However, the scorer also reports accuracy, precision and recall.


## Baselines

The [baselines](baselines) module currently contains a majority, random and a simple n-gram baseline.

Baseline Results for the task on Dev-Test set

| Model                      | micro-F1 |
|----------------------------|----------|
| Random Baseline            | 0.3244   |
| Majority Baseline          | 0.2210   |
| n-gram Baseline            | 0.4436   |

## Format checker

The format checkers for the task are located in the [format_checker](format_checker) module of the project. The format checker verifies that your generated results file complies with the expected format.

Before running the format checker please install all prerequisites,
```
pip install -r requirements.txt
```

To launch it, please run the following command:

```
python format_checker/task.py -p paths_to_your_results_files
```

##### Example
```
python format_checker/task.py -p ./task.txt
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
- The output file must be named task.tsv. Failure to follow this naming convention will result in an error on the leaderboard.
- You are required to compress the .tsv file into a .zip file (for example, zip task.zip task.tsv) and submit it via the Codalab page.
- Please include your team name and a description of your method with each submission.
- You are permitted to submit a maximum of 50 submissions per day for the task.


### Submission Site
**TBA**


## Licensing
The dataset is free for general research use.

## Citation
There are various papers associated with the task. Details for the papers specific to the task as well as an overall overview will be posted here as they come out. Bib entries for each paper are included here. For your convenience, the [bib file](bibtex/bibliography.bib) is available as well.

```
to appear
```

```
@inproceedings{islam-etal-2021-sentnob-dataset,
    title = "{S}ent{N}o{B}: A Dataset for Analysing Sentiment on Noisy {B}angla Texts",
    author = "Islam, Khondoker Ittehadul  and
      Kar, Sudipta  and
      Islam, Md Saiful  and
      Amin, Mohammad Ruhul",
    booktitle = "Findings of the Association for Computational Linguistics: EMNLP 2021",
    month = nov,
    year = "2021",
    address = "Punta Cana, Dominican Republic",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.findings-emnlp.278",
    doi = "10.18653/v1/2021.findings-emnlp.278",
    pages = "3265--3271",
}
```

## Organizers
- Md. Arid Hasan, GRA, University of New Brunswick
- Shudipta Das, Daffodil International University
- Afiyat Anjum, Daffodil International University
- Anika Anjum, Daffodil International University
- [Dr. Firoj Alam](http://sites.google.com/site/firojalam/), Scientist, Qatar Computing Research Institute
