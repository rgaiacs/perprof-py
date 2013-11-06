"""
The functions related with the perform (not the output).
"""

import pprint
import math
from . import parse

def load_data(setup):
    """
    Load the data.

    :param setup: the setup configurations
    :type setup: main.PerProfSetup
    """
    data = {}
    for f in setup.get_files():
        data_tmp, solver_name = parse.parse_file(f)
        data[solver_name] = data_tmp
    return data

class Pdata:
    def __init__(self, setup):
        self.data = load_data(setup)
        self.cache = setup.using_cache()
        self.force = setup.using_force()
        self.semilog = setup.using_semilog()

    def __repr__(self):
        try:
            self.solvers
        except:
            self.get_set_solvers()
        try:
            self.problems
        except:
            self.get_set_problems()

        for s in self.solvers:
            print('{:>8}'.format(s), end='  ')
        print()

        for p in self.problems:
            print('{:>8}'.format(p), end='  ')
            for s in self.solvers:
                print('{:8.4}'.format(self.data[s][p]), end='  ')
            print()

        print('times = ', end=' ')
        for t in self.times:
            print('{:.4}'.format(t), end=' ')
        print()

        print('perf_functions:')
        pprint.pprint(self.perf_functions)

        return ''

    def get_set_solvers(self):
        try:
            self.solvers
        except:
            self.solvers = self.data.keys()
        return self.solvers

    def get_set_problems(self):
        try:
            self.problems
            self.number_problems
        except:
            p = set()
            for i in self.data.keys():
                for j in self.data[i].keys():
                    p.add(j)
            self.problems = p
            self.number_problems = len(p)
        return self.problems

    def scale(self):
        """
        Scale time.
        """
        try:
            self.solvers
        except:
            self.get_set_solvers()
        try:
            self.problems
        except:
            self.get_set_problems()

        self.times = set()
        for p in self.problems:
            min_time = float('inf')
            for s in self.solvers:
                try:
                    if self.data[s][p] < min_time:
                        min_time = self.data[s][p]
                except:
                    pass
            for s in self.solvers:
                try:
                    self.data[s][p] = self.data[s][p] / min_time
                except:
                    self.data[s][p] = float('inf')
                if (self.data[s][p] < float('inf')):
                    self.times.add(self.data[s][p])
        self.times = [x for x in self.times]
        self.times.sort()

    def plot(self):
        """
        This should be implemented by a child of this class.
        """
        raise NotImplementedError()