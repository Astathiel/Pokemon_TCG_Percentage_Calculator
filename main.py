packs = 230

cards_per_pack = 5

total_pulls = packs * cards_per_pack

percentage_cynthia = 0.00041

percentage_fail = 1 - percentage_cynthia

percentage_fail_total = percentage_fail ** total_pulls

percentage_success = 1 - percentage_fail_total

chance_percentage = percentage_success * 100

print(f"Total pulls: {total_pulls}")
print(f"Chance of pulling Cynthia in {packs} packs: {chance_percentage:.2f}%")

