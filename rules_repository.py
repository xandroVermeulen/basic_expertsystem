from collections import defaultdict

#structure that holds one rule. A rule contains: needed facts, possible conclusion facts and/or possible triggers
class Rule:
    def to_string(self):
        return (" AND ".join(self.needed_facts) + " ==> " +", ".join(self.conclusion_facts)
        + ((" + triggers: " + ", ".join(self.conclusion_triggers)) if (len(self.conclusion_triggers) > 0) else ""))
   
    def __init__(self, needed_facts, conclusion_facts, conclusion_triggers):
        self.needed_facts = needed_facts
        self.conclusion_facts = conclusion_facts
        self.conclusion_triggers = conclusion_triggers

#structure that holds all different rulesets. Different rulesets can be build for different types of smokers
rulesets = {
        "standard": [
            Rule(['A:1','B:laag'],['C:1'],['Trigger_A'])       
        ],
        "test":[
            Rule(['A:1', 'B:1'],['C:1'],[]),  
            Rule(['C:1','D:1', 'A:1'],['E:1'],[]),  
            Rule(['E:1'],[],['Warn about E']),  
        ]
}
      
#returns a structure needed for the expertsystem  
def get_needed_in_rule_dict(ruleset_name):
    needed_in_rule_dict = defaultdict(list)
    index = 0
    for rule in rulesets[ruleset_name]:
        needed_facts = rule.needed_facts
        for fact in needed_facts:
            needed_in_rule_dict[fact].append(index)
        index += 1
    print("needed_in_rule_dict: "+str(needed_in_rule_dict))
    return needed_in_rule_dict     

#returns a structure needed for the expertsystem 
def get_facts_still_needed_counters(ruleset_name):
    facts_still_needed_counters = []
    for rule in rulesets[ruleset_name]:
        facts_still_needed_counters.append(len(rule.needed_facts))
    print("facts_still_needed_counters: "+str(facts_still_needed_counters))
    return facts_still_needed_counters
    
#get the conclusion/triggers from a certain rule
def execute_rule(ruleset_name, rule_index):
    print("exec: "+rulesets[ruleset_name][rule_index].to_string())
    return [rulesets[ruleset_name][rule_index].conclusion_facts, rulesets[ruleset_name][rule_index].conclusion_triggers]

def print_ruleset(name):
    for rule in rulesets[name]:
       print(rule.to_string())