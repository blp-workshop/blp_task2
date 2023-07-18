# Sentiment Analysis Shared Task at [BLP Workshop @EMNLP 2023](https://blp-workshop.github.io/)

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
- [Organizers](#Credits)

## Important Dates
- **16 July 2023:** Registration on codalab and beginning of the development cycle
- **15 August 2023:** Beginning of the evaluation cycle (test sets release and run submission)
- **18 August 2023:** End of the evaluation cycle
- **20 August 2023:** Publish rank list and share paper submission details
- **12 September 2023:** Deadline for the submission of working notes
- **10 October 2023:** Notification of acceptance
- **18 October 2023:** Camera-ready due
- **8 December 2023:** Workshop co-located with EMNLP (Singapore)


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
For a brief overview of the dataset, kindly refer to the *README.md* file located in the data directory.


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
The scorer for the task is located in the [scorer](scorer) module of the project. The scorer will report official evaluation metrics and other metrics of a prediction file. The scorer invokes the format checker for the task to verify the output is properly shaped. It also handles checking if the provided predictions file contains all tweets from the gold one.


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
| Random Baseline            | 0.3389   |
| Majority Baseline          | 0.4962   |
| n-gram Baseline            | 0.5736   |

## Format checker

The format checkers for the task are located in the [format_checker](format_checker) module of the project. The format checker verifies that your generated results file complies with the expected format.

Before running the format checker please install all prerequisites,
```
pip install -r requirements.txt
```

To launch it, please run the following command:

```
python format_checker/task.py -p results_files
```

##### Example
```
python format_checker/task.py -p ./task.txt
```
**results_files**: can be one path or space-separated list of paths


<!-- **Note that the checker cannot verify whether the prediction file you submit contains all lines, because it does not have access to the corresponding gold file.** -->


## Submission

### Guidelines
Evaluation consists of two phases:

1. **Development phase:** This phase involves working on the *dev-test set*.
2. **Evaluation phase:** This phase involves working on the *test set*, which will be released during the ***evaluation cycle***.

For each phase, please adhere to the following guidelines:

- We request each team to establish and manage a single account for all submissions. Hence, all runs should be submitted through the same account. Any submissions made from multiple accounts by the same team may lead to your system being not ranked from the final ranking in the overview paper.
- The most recently uploaded file on the leaderboard will serve as your final submission.
- Adhere strictly to the naming convention for the output file, which must be labeled as 'task.tsv'. Deviation from this standard could trigger an error on the leaderboard.
- Submission protocol requires you to compress the '.tsv' file into a '.zip' file (for instance, zip task.zip task.tsv) and submit it through the Codalab page.
- With each submission, ensure to include your team name along with a brief explanation of your methodology.
- Each team is allowed a maximum of 50 submissions per day for the given task. Please adhere to this limit.


### Submission Site
[https://codalab.lisn.upsaclay.fr/competitions/14587](https://codalab.lisn.upsaclay.fr/competitions/14587)


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

## Communication
Please join us in Slack channel for discussion and doubts:
 - [Slack](https://join.slack.com/t/blpworkshop/shared_invite/zt-1ryu9eyac-7fevK9A4_Bt~qN_eCK349g)

## Organizers
- [Md. Arid Hasan](https://sites.google.com/view/aridhasan), GRA, University of New Brunswick
- [Firoj Alam](http://sites.google.com/site/firojalam/), Scientist, Qatar Computing Research Institute
- Shudipta Das, Daffodil International University
- Afiyat Anjum, Daffodil International University
- Anika Anjum, Daffodil International University