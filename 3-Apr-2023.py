def parse_rule(rule):
    tokens = rule.split(" ")
    condition = tokens[1:-2]
    result_var = tokens[-1]
    return condition, result_var


def evaluate_condition(condition, facts, vars):
    stack = []
    res = False
    can_be_parsed = False
    for token in condition:
        stack.append(token)

    for token in condition:
        if token in facts:
            stack[stack.index(token)] = facts[token]
        if token in vars and token not in facts:
            return can_be_parsed, res

    for token in condition:
        if token == "NOT":
            stack[stack.index(token) + 1] = not stack[stack.index(token) + 1]
            del stack[stack.index(token)]

    for token in condition:
        if token == "AND":
            res = stack[stack.index(token) - 1] and stack[stack.index(token) + 1]
        elif token == "OR":
            res = stack[stack.index(token) - 1] or stack[stack.index(token) + 1]

    can_be_parsed = True

    return can_be_parsed, res


def Inference_engine(num_vars, variable_names, rules, facts):
    fired_rules = rules
    res = []
    while(len(fired_rules) != 0):
        for rule in rules:
            if rule in fired_rules:
                condition, result_var = parse_rule(rule)
            else:
                continue
            can_parse, result = evaluate_condition(condition, facts, variable_names)
            if can_parse:
                fired_rules.remove(rule)
                res.append(rule)
                facts[result_var] = result
    return res


if __name__ == "__main__":
    # num_vars = int(input("Enter no. of variables : "))
    # variable_names = []
    # for i in range(num_vars):
    #     variable_names.append(input("Enter variable name : "))
    # rules = []
    # for i in range(3):
    #     rules.append(input("Enter rule {}: ".format(i+1)))
    # facts = {}
    # for i in range(2):
    #     var = input("Enter variable {}: ".format(i+1))
    #     val = input("Enter value of {}: ".format(var))
    #     facts[var] = val

    num_vars = 5
    variable_names = ["A", "B", "C", "D", "E"]
    rules = [
        "IF A AND B THEN C",
        "IF E AND NOT A THEN D",
        "IF C OR NOT B OR A THEN E",
    ]
    facts = {
        "A": True,
        "B": False,
    }
    print(Inference_engine(num_vars, variable_names, rules, facts))
