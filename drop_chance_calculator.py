import math

cards_per_pack = 5

def probability_calculator():
    print("-- Pokemon TCG Drop Chance Calculator --")
    print("Type 'exit' at any prompt to quit.")
    
    while True:
        try:

            rarity_input = input("Enter rarity drop rate  of the 5th card in % (e.g. 2 for 2 percentage, 0.5 for 0.500 percentage): ")
            if rarity_input.lower() == 'exit': break
            rarity_rate = float(rarity_input)

            pool_input = input("Enter total amount of cards in this rarity category: ")
            if pool_input.lower() == 'exit': break
            pool_size = int(pool_input)

            packs_input = input("Enter number of packs to open: ")
            if packs_input.lower() == 'exit': break
            packs = int(packs_input)
            

            
            # Calculations
            percentage_specific_card = (rarity_rate / 100) / pool_size
            
            total_pulls = packs * cards_per_pack
            
            percentage_fail_once = 1 - percentage_specific_card
            
            percentage_fail_total = math.pow(percentage_fail_once, total_pulls)
            
            percentage_success = 1 - percentage_fail_total
            
            print("-" * 40)
            print(f"Total Cards Pulled: {total_pulls}")
            print(f"Chance to get specific card within the category: {percentage_specific_card * 100:.6f}%")
            print(f"ODDS OF PULLING THE WANTED CARD OUT OF TOTAL PULLS {total_pulls} is: {percentage_success * 100:.4f}%")
            print("-" * 40 + "\n")

        except ValueError:
            print("Error: Please enter valid numbers. Try again.\n")
        except ZeroDivisionError:
            print("Error: Pool size cannot be zero.\n")


if __name__ == "__main__":
    probability_calculator()

