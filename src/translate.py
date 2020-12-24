
# read file from import directory
# mine it and return result to export directory


import pm4py
import os
import helper
from pathlib import Path
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.objects.conversion.process_tree import converter
CURRENT = os.getcwd()


async def translate():

    """[async function for translating process tree to BPMN 2.0 model] """
    relativePath = os.path.join("upload", "file.bpmn")

    # delete any existing files in upload dir

    # parse tree to local var

    # convert process tree to BPMN
    bpmn_graph = converter.apply(tree, variant=converter.Variants.TO_BPMN)

    # delete any existing files in export dir

    # export to valid BPMN model
    pm4py.write_bpmn(bpmn_graph, "export.bpmn", enable_layout=True)

    # move file to export dir
    current = os.path.abspath(".")
    os.rename(os.path.join(current, "export.bpmn"),
              os.path.join(current, "export/export.bpmn"))
