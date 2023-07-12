import re
from typing import Dict, List, Optional

from constraints import Constraint, CSP, V, D

the_name = r'(\w*):.*'
position = r"\w*:I'm in (\d).. position"
man_front = r"\w*:The man in front of me is (\w*)\."
man_behind = r"\w*:The man behind me is (\w*)\."
num_front = r"\w*:There (?:is|are) (\d) people in front of me\."
num_behind = r"\w*:There (?:is|are) (\d) people behind me\."

POS = 'position'
MF = 'man front'
MB = 'man behind'
NF = 'num front'
NB = 'num behind'

rules = [
    position, man_front, man_behind, num_front, num_behind
]

tokens = [
    POS, MF, MB, NF, NB
]


class BaseConstraint(Constraint[V, D]):

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        if len(set(assignment.values())) != len(assignment.values()):
            return False
        return True


class PositionConstraint(BaseConstraint[str, int]):
    def __init__(self, name: str, pos: int, negative: bool = False) -> None:
        super().__init__([name])
        self.name: str = name
        self.pos: int = pos
        self.negative = negative

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        if self.name not in assignment:
            return True
        if not super().satisfied((assignment)):
            return False

        if not self.negative:
            return assignment[self.name] == self.pos
        return assignment[self.name] != self.pos


class RelativePositionConstraint(BaseConstraint[str, str]):
    def __init__(self, first: str, second: str, negative: bool = False) -> None:
        super().__init__([first, second])
        self.first: str = first
        self.second: str = second
        self.negative = negative

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        if self.first not in assignment or self.second not in assignment:
            return True
        if not super().satisfied((assignment)):
            return False

        if not self.negative:
            return assignment[self.first] == assignment[self.second] - 1
        return assignment[self.first] != assignment[self.second] - 1


def parse_rules(conversation):
    names = set()
    these_rules = []
    for sentence in conversation:
        this = re.match(the_name, sentence).group(1)
        names.add(this)
        for token, rule in zip(tokens, rules):
            if match := re.match(rule, sentence):
                if match.group(1) is None:
                    raise Exception(f'{rule} {sentence}')
                these_rules.append((this, token, match.group(1)))
                break
        else:
            raise Exception(f'Unmatched sentence: {sentence}')

    return names, these_rules


def apply_constraints(the_name, names, name_rules, negatives):
    variables: List[str] = list(names)
    domains: Dict[str, List[int]] = {}
    for variable in variables:
        domains[variable] = list(range(len(names)))
    csp: CSP[str, str] = CSP(variables, domains)

    for rule in name_rules:
        handle_rule(rule, names, csp)
    for rule in negatives:
        handle_rule(rule, names, csp, negative=True)
    solution = csp.backtracking_search()
    print(the_name, solution)
    return bool(solution)

def handle_rule(rule, names, csp, negative=False):
    name, token, value = rule
    if token == POS:
        csp.add_constraint(PositionConstraint(name, int(value) - 1, negative=negative))
    elif token == MF:
        csp.add_constraint(RelativePositionConstraint(value, name, negative=negative))
    elif token == MB:
        csp.add_constraint(RelativePositionConstraint(name, value, negative=negative))
    elif token == NF:
        csp.add_constraint(PositionConstraint(name, int(value), negative=negative))
    elif token == NB:
        behind = int(value)
        pos = len(names) - (behind + 1)
        csp.add_constraint(PositionConstraint(name, pos, negative=negative))
    else:
        raise Exception(f'Unknown token: {token}')


def find_out_mr_wrong(conversation):
    names, rules = parse_rules(conversation)

    # create a set of domains/constraints for the rules ignoring one person
    # if we can solve the constraints we have found a liar.
    # For the liar we make negative constraints, only finding a solution if
    # their statements are explicitly wrong.

    results = []
    for name in names:
        name_rules = [rule for rule in rules if rule[0] != name]
        negatives = [rule for rule in rules if rule[0] == name]
        result = apply_constraints(name, names, name_rules, negatives)
        results.append((name, result))

    found = set()
    for name, wrong in results:
        if wrong:
            found.add(name)
    print(f'Found {found}')
    if len(found) == 1:
        return list(found)[0]
    return None
