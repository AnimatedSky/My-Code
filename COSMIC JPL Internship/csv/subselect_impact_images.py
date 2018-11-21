#!/usr/bin/env python
import os
import csv
import json
from shutil import copy
from progressbar import ProgressBar, ETA, Bar
from collections import defaultdict

#from make_impact_manifest import main as make_manifest

WORKFLOW = 'Fresh Impact Pre-Filter'
FILTER_CLASSES = ['Other']

def main(classifications, inputdir, outputdir):

    with open(classifications, 'r') as f:
        reader = csv.reader(f)
        header = None
        data = defaultdict(list)
        for line in reader:
            if header is None:
                header = line
                continue
            for h, column in zip(header, line):
                data[h].append(column)

    workflow = data['workflow_name']
    annotations = map(json.loads, data['annotations'])
    subjects = map(json.loads, data['subject_data'])

    jobs = []
    for w, a, s in zip(workflow, annotations, subjects):
        assert(len(s) == 1)
        if w != WORKFLOW: continue
        cls = a[0]['value']
        if cls in FILTER_CLASSES: continue
        img = s.values().pop()['image']
        jobs.append((
            os.path.join(inputdir, img),
            os.path.join(outputdir, img),
        ))

    progress = ProgressBar(widgets=['Copying files: ', Bar('='), ' ', ETA()])
    for job in progress(jobs):
        copy(*job)

   # make_manifest(outputdir, 'jpg')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    parser.add_argument('classifications')
    parser.add_argument('inputdir')
    parser.add_argument('outputdir')

    args = parser.parse_args()
    main(**vars(args))
