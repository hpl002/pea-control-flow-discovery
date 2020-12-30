import os
import helper
import evaluator
from pathlib import Path
from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.algo.discovery.inductive import algorithm as inductive_miner
from pm4py.objects.conversion.process_tree import converter
from pm4py.objects.process_tree.exporter import exporter as ptml_exporter
from pm4py.objects.process_tree.importer import importer as ptml_importer
from pm4py.write import write_bpmn

CURRENT = os.getcwd()


def mine(filename):
    """[mines .xes to process model / process tree] """
    log = xes_importer.apply(os.path.join("upload", filename))
    tree = inductive_miner.apply_tree(log)
    helper.wipe_dir(os.path.join(CURRENT, "export"))
    name = Path(filename).stem
    ptml_exporter.apply(tree, name + ".ptml")
    helper.mv_file_to_export_dir(CURRENT, name + ".ptml")


def translate(filename):
    """[translates process tree to BPMN 2.0 model] """
    tree = ptml_importer.apply(os.path.join("upload", filename))
    bpmn_graph = converter.apply(tree, variant=converter.Variants.TO_BPMN)
    helper.wipe_dir(os.path.join(CURRENT, "export"))
    name = Path(filename).stem
    write_bpmn(bpmn_graph, name + ".bpmn", enable_layout=True)
    helper.mv_file_to_export_dir(CURRENT, name + ".bpmn")


# take dict as arg
# check  that the object has all expexted keys
# execute all "enabled functions"


def evaluate(funcs, filename_tree, filename_log):
    """[execute all truthy eval function in funcs object] """
    tree = ptml_importer.apply(os.path.join("upload", filename_tree))
    log = xes_importer.apply(os.path.join("upload", filename_log))

    # transform proces tree to petri net
    net, im, fm = converter.apply(tree)
    # perform evaluation
    e = evaluator.ModelLogEvaluator(log, net, im, fm)

    for key in funcs:
        if funcs[key] == True:
            func = getattr(e, key)
            func()
            funcs[key] = func()
    return funcs
