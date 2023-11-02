# -*- coding: utf-8 -*-
"""raw_to_evaluation_datasets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12PzukchhxQEOBuouOJrFnGegqIo9aWqn
"""

import json
import sys

class Logger(object):
    def __init__(self, filename="test-annotations.txt"): # change the file name (e.g., train-annotations.txt, dev-annotations.txt, ood-anntations.txt, etc.)
        self.filename = filename
        self.terminal = sys.stdout
        self.log = None

    def open(self):
        self.log = open(self.filename, "a")

    def close(self):
        if self.log:
            self.log.close()

    def write(self, message):
        self.terminal.write(message)
        if self.log:
            self.log.write(message)

    def flush(self):
        pass

# Create an instance of the Logger class
logger = Logger("test-annotations.txt")
logger.open()

sys.stdout = logger

# Open the JSON file (e.g., train.json, dev.json, test.json, ood.json, etc.)
with open('test.json') as json_file:
    data = json.load(json_file)

# Iterate over each item in the JSON data
for item in data:
    # Extract the will text
    will_text = item['data']['text']
    sys.stdout.write("Will Text: {}\n".format(will_text))
    sys.stdout.write("---\n")

    # Extract and print the annotations
    annotations = item['annotations']
    for annotation in annotations:
        annotation_id = annotation['id']
        sys.stdout.write("Annotation ID: {}\n".format(annotation_id))
        sys.stdout.write("---\n")

        if 'result' in annotation and annotation['result']:
            results = annotation['result']
            for result in results:
                if 'value' in result: # add the entities you wish to evaluate below (e.g., EXECUTOR, WITNESS, etc.)
                    if result['value']['labels'] == ['TESTATOR'] or result['value']['labels'] == ['BENEFICIARY'] or result['value']['labels'] == ['WILL'] or result['value']['labels'] == ['ASSET']:
                        id = result['id']
                        value = result['value']
                        annotation_text = value['text']
                        start_id = value['start']
                        end_id = value['end']
                        annotation_labels = value['labels']
                        sys.stdout.write("Entity ID: {}\n".format(id))
                        sys.stdout.write("Annotation Text: {}\n".format(annotation_text))
                        sys.stdout.write("Start Index: {}\n".format(start_id))
                        sys.stdout.write("End Index: {}\n".format(end_id))
                        sys.stdout.write("Annotation Labels: {}\n".format(annotation_labels))
                        sys.stdout.write("---\n")
                if result['type'] == "relation": # add the relations you wish to evaluate below (e.g., 'TESTATOR-EXECUTOR', 'TESTATOR-WITNESS', etc.)
                    if result['labels'] == ['BENEFICIARY-ASSET'] or result['labels'] == ['TESTATOR-ASSET'] or result['labels'] == ['TESTATOR-BENEFICIARY'] or result['labels'] == ['TESTATOR-WILL']:
                        to_id = result['to_id']
                        from_id = result['from_id']
                        relation_labels = result['labels']
                        sys.stdout.write("Relation Labels: {}\n".format(relation_labels))
                        sys.stdout.write("to_id: {}\n".format(to_id))
                        sys.stdout.write("from_id: {}\n".format(from_id))
                        sys.stdout.write("---\n")
    sys.stdout.write("===================================\n")

logger.close()