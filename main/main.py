
import pm4py
import os
from pathlib import Path
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.objects.conversion.process_tree import converter

# import
relativePath = os.path.join("test-data", "running-example.xes")
log = xes_importer.apply(relativePath)

# mine
tree = inductive_miner.apply_tree(log)

# convert process tree to BPMN
bpmn_graph = converter.apply(tree, variant=converter.Variants.TO_BPMN)

# export to valid BPMN model
pm4py.write_bpmn(bpmn_graph, "export.bpmn", enable_layout=True)
