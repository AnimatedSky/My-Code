import csv
import json
from collections import defaultdict


#-----CREATE CLASS STRUCTURE-------
class LabeledImpact(object):
    def __init__(self, metadata, polygons):
        self.metadata = metadata
        self.polygons = polygons
class SubjectMetadata(object):
    def __init__(self, user, time, image):
        self.user = user
        self.time = time
        self.image = image
class LabeledPolygon(object):
    def __init__(self, label, value, points):
        self.label = label
        self.form = form
        self.points = points

#------PULLS DATA FROM CSV FILE-------
with open ('draw-boundaries-around-fresh-new-impact-craters-on-mars-classifications.csv', 'r') as FreshImpacts:
    reader = csv.reader(FreshImpacts)
    header = None
    data = defaultdict(list)#defaultdict
    for line in reader:
        if header is None:
            header = line
            continue
        for h, column in zip(header, line): #zip
            data[h].append(column) #

#-----DEFINE NOT JSON DATA------
user = data['user_name']
time = data['created_at']

#-----PULLING JSON FILES---------
annotations = list(map(json.loads, data['annotations']))
subjects = list(map(json.loads, data['subject_data']))

#-----PULLS IMAGE NAME---------
image = []
for num in range(len(subjects)):
    image.append(list(subjects[num].values()).pop()['image'])

#------PULLS REST OF DATA-----
labeled_impacts = []
for u,t,a,s in zip(user,time, annotations, subjects):#RE-ZIP DATA TO MORE LEGIBLE
    assert (len(a)==1)
    annotation = a[0]
    label = annotation['task_label']
    values = annotation['value']
    metadata = SubjectMetadata(user, time, image)
    polygons = []
    for value in values:
        points = value['points']
        form = value['tool_label']
        s_points = []
        for point in points:
        	s_points.append((point['x'], point['y']))
        polygon = LabeledPolygon(label, form, points)
        polygons.append(polygon)
    labeled_impact = LabeledImpact(metadata, polygons)
    labeled_impacts.append(labeled_impact)

#------------TEST-------------
print(labeled_impacts[0].polygons[0].points[0])