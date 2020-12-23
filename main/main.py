import os
# importer
from pm4py.objects.log.importer.xes import importer as xes_importer
# discovery algorithm
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
# visualizer
from pm4py.visualization.process_tree import visualizer as pt_visualizer

filePath = os.path.join("tests", "input_data", "running-example.xes")

log = xes_importer.apply(filePath)

net, initial_marking, final_marking = inductive_miner.apply(log)


# comment
