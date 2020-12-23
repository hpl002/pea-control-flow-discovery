
import pm4py
import os
from pathlib import Path
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.objects.conversion.process_tree import converter

relativePath = os.path.join("test-data", "running-example.xes")

# import
log = xes_importer.apply(relativePath)

# mine
tree = inductive_miner.apply_tree(log)

# convert process tree to BPMN
bpmn_graph = converter.apply(tree, variant=converter.Variants.TO_BPMN)

# export to valid BPMN model
pm4py.write_bpmn(bpmn_graph, "export.bpmn", enable_layout=True)

# move file to export dir
current = os.path.abspath(".")
os.rename(os.path.join(current, "export.bpmn"),
          os.path.join(current, "main/export/export.bpmn"))
