import os
import helper
from pathlib import Path
from pm4py.evaluation.replay_fitness import evaluator as replay_fitness_evaluator
from pm4py.evaluation.precision import evaluator as precision_evaluator
from pm4py.evaluation.generalization import evaluator as generalization_evaluator
from pm4py.evaluation.simplicity import evaluator as simplicity_evaluator


class ModelLogEvaluator:
    def __init__(self, log, net, im, fm):
        self.log = log  # event log
        self.net = net  # petri-net
        self.im = im  # initial marking
        self.fm = fm  # final marking

    def replayFitnessTokenBased(self):
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
            self.log, self.net, self.im, self.fm, variant=replay_fitness_evaluator.Variants.TOKEN_BASED)
        return r

    def replayFitnessAlignmentBased(self):
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
            self.log, self.net, self.im, self.fm, variant=replay_fitness_evaluator.Variants.ALIGNMENT_BASED)
        return r

    def precisionETConformance(self):
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
            self.log, self.net, self.im, self.fm, variant=precision_evaluator.Variants.ETCONFORMANCE_TOKEN)
        return r

    def precisionAlignETConformance(self):
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
            self.log, self.net, self.im, self.fm, variant=precision_evaluator.Variants.ALIGN_ETCONFORMANCE)
        return r

    def generalization(self):
        """[get generalization score]

        Args:
            log ([log]): [event log]
            net ([net]): [petri net]
            im ([initial_marking]): [initial marking]
            fm ([final marking]): [final marking]

        Returns:
            [int]: [score]
        """
        r = generalization_evaluator.apply(
            self.log, self.net, self.im, self.fm)
        return r

    def simplicity(self):
        """[get simplicity score]

        Args:
            net ([net]): [petri net]

        Returns:
            [int]: [score]
        """
        r = simplicity_evaluator.apply(self.net)
        return r
