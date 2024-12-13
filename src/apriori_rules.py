from apyori import apriori

def generate_rules(transactions, min_support=0.001, min_confidence=0.6, min_lift=1.0, max_length=3):
    frequent_itemsets = apriori(transactions, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift, max_length=max_length)
    rules = list(frequent_itemsets)
    return rules
