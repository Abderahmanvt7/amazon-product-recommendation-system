def recommend(item, rules):
    recommendations = []
    for rule in rules:
        if item in rule.items:
            consequent = rule.ordered_statistics[0].items_add
            recommendations.append((consequent, rule.ordered_statistics[0].confidence, rule.ordered_statistics[0].lift))
    recommendations.sort(key=lambda x: (x[1], x[2]), reverse=True)
    return recommendations[:5]
