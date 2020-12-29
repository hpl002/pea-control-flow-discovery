import os
import helper
from pathlib import Path
from pm4py.evaluation.replay_fitness import evaluator as replay_fitness_evaluator
from pm4py.evaluation.precision import evaluator as precision_evaluator
from pm4py.evaluation.generalization import evaluator as generalization_evaluator
from pm4py.evaluation.simplicity import evaluator as simplicity_evaluator


def evaluate():
    """[performs log-model evaluation] """
    log = os.path.join("upload", "file.ptml")
    tree = ptml_importer.apply(log)
    bpmn_graph = converter.apply(tree, variant=converter.Variants.TO_BPMN)
    helper.wipe_dir(os.path.join(CURRENT, "export"))
    write_bpmn(bpmn_graph, "file.bpmn", enable_layout=True)
    helper.mv_file_to_export_dir(CURRENT, "file.bpmn")


def replayFitnessTokenBased(log, net, im, fm):
    """[get fitness using token-based replay]

    Args:
        log ([log]): [event log]
        net ([net]): [petri net]
        im ([initial_marking]): [initial marking]
        fm ([final marking]): [final marking]

    Returns:
        [int]: [score]
    """
    r = replay_fitness_evaluator.apply(
        log, net, im, fm, variant=replay_fitness_evaluator.Variants.TOKEN_BASED)
    return r


def replayFitnessAlignmentBased(log, net, im, fm):
    """[get fitness using token-based replay]

    Args:
        log ([log]): [event log]
        net ([net]): [petri net]
        im ([initial_marking]): [initial marking]
        fm ([final marking]): [final marking]

    Returns:
        [int]: [score]
    """
    r = replay_fitness_evaluator.apply(
        log, net, im, fm, variant=replay_fitness_evaluator.Variants.ALIGNMENT_BASED)
    return r


def precisionETConformance(log, net, im, fm):
    """[get precision using ETConformance, which is using token-based replay]

    Args:
        log ([log]): [event log]
        net ([net]): [petri net]
        im ([initial_marking]): [initial marking]
        fm ([final marking]): [final marking]

    Returns:
        [int]: [score]
    """
    r = precision_evaluator.apply(
        log, net, im, fm, variant=precision_evaluator.Variants.ETCONFORMANCE_TOKEN)
    return r


def precisionAlignETConformance(log, net, im, fm):
    """[get precision using Align-ETConformance, which is using alignment]

    Args:
        log ([log]): [event log]
        net ([net]): [petri net]
        im ([initial_marking]): [initial marking]
        fm ([final marking]): [final marking]

    Returns:
        [int]: [score]
    """
    r = precision_evaluator.apply(
        log, net, im, fm, variant=precision_evaluator.Variants.ALIGN_ETCONFORMANCE)
    return r


def generalization(log, net, im, fm):
    """[get generalization score]

    Args:
        log ([log]): [event log]
        net ([net]): [petri net]
        im ([initial_marking]): [initial marking]
        fm ([final marking]): [final marking]

    Returns:
        [int]: [score]
    """
    r = generalization_evaluator.apply(log, net, im, fm)
    return r


def simplicity(net):
    """[get simplicity score]

    Args:
        net ([net]): [petri net]

    Returns:
        [int]: [score]
    """
    r = simplicity_evaluator.apply(net)
    return r
