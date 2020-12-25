
# read file from import directory
# mine it and return result to export directory


import os
import pm4py
import helper
from pathlib import Path
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.objects.conversion.process_tree import converter
from pm4py.objects.process_tree.exporter import exporter as ptml_exporter
CURRENT = os.getcwd()


def mine():
    """[mines .xes to process model / process tree] """

    log = xes_importer.apply(os.path.join("upload", "file.xes"))
    tree = inductive_miner.apply_tree(log)
    helper.wipe_dir(os.path.join(CURRENT, "export"))
    ptml_exporter.apply(tree, "file.ptml")
    helper.mv_file_to_export_dir(CURRENT, "file.ptml")
