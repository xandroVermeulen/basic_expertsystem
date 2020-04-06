import rules_repository as rules

class Expertsystem_engine:
    def __init__(self, facts, ruleset_name = "test"):
        if facts == None or len(facts) == 0:
            return None
        self.facts = facts
        self.ruleset_name = ruleset_name
        self.seen_facts = facts
        rules.print_ruleset(ruleset_name)
        self.facts_still_needed_counters = rules.get_facts_still_needed_counters(ruleset_name)
        self.needed_in_rule_dict = rules.get_needed_in_rule_dict(ruleset_name)
        self.trigger_list = []

    def start_forward_chaining(self): 
        while self.facts and len(self.facts) > 0 :
            current_fact = self.facts.pop(0)
            needed_in_rules = self.needed_in_rule_dict[current_fact]
            for rule_index in needed_in_rules:
                self.facts_still_needed_counters[rule_index] -= 1
                if self.facts_still_needed_counters[rule_index] == 0:
                    conclusion_facts, conclusion_triggers = rules.execute_rule(self.ruleset_name, rule_index)
                    self.trigger_list.extend(conclusion_triggers)
                    for conc_fact in conclusion_facts:
                        if conc_fact not in self.seen_facts:
                            self.seen_facts.append(conc_fact)
                            self.facts.append(conc_fact) 
    
def check_triggers(facts, ruleset_name):
    expertsystem = Expertsystem_engine(facts, ruleset_name)
    expertsystem.start_forward_chaining()
    print(str(expertsystem.trigger_list))

check_triggers(['A:1','B:laag'], "standard")