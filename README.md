# Task 7

## Objectives
The objective of this task is to analyze data from a kaggle challenge that envolves convert prediction
showed in the notebook. All the information is there with the description
of the thought process. <br>
The other objective is to create an app that predicts via json that can
accept either a raw json string, or a json file to do the prediction

## How to use the app
The way you use the app is to clone this repo and simply use python3 main.py raw_json | file.json <br>
The json must be orient record(normal json we see in APIs), and must contain 88 elements from 0 to 87
with float values <br>
After passing, the app will check if it is a raw json or json file or invalid and proceed to output in json format
string the results of the predictions: <br>
0 for not converted <br>
1 for converted

## Why is the training csv file not availabe?
The link to the csv file is in the notebook, it's not displayable in this repo because it's 400MB,
which exceeds the GitHub maximum file size 
