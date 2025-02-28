import os

# Initialize counts for all categories
shiny_after_puzzle_total = 0
shiny_without_puzzle_total = 0
no_rare_fish_after_puzzle_total = 0
no_rare_fish_without_puzzle_total = 0

# List all files in the 'logs' directory
log_files = os.listdir("logs")
opened_logs = 0

# Process each log file
for log_file in log_files:
    opened_logs += 1
    # Read logs
    with open(os.path.join("logs", log_file), "r", encoding="ISO-8859-1") as file:
        logs = file.readlines()

    shiny_after_puzzle = 0
    shiny_without_puzzle = 0
    no_rare_fish_after_puzzle = 0
    no_rare_fish_without_puzzle = 0

    # Logs processing
    for i, line in enumerate(logs):
        if "Wild pokémon appeared!" in line:
            # Check if the previous line [line - 2] contains the message "Solving puzzle..."
            # Also check if the line before [line - 1] contains "..."
            if "..." in logs[i - 1] and "Solving puzzle..." in logs[i - 2]:
                shiny_after_puzzle += 1
            else:
                shiny_without_puzzle += 1
        
        elif "Solving puzzle..." in line:
            # If there is "..." after solving the puzzle, consider it as "No Rare Fish" after the puzzle
            if i + 2 < len(logs) and "..." in logs[i + 2]:
                no_rare_fish_after_puzzle += 1
        
        elif "..." in line:
            # If there is "..." and there is no "Solving puzzle..." before, consider it as "No Rare Fish" without puzzle
            if i > 0 and "Solving puzzle..." not in logs[i - 1]:
                no_rare_fish_without_puzzle += 1

    # Accumulate counts for each category
    shiny_after_puzzle_total += shiny_after_puzzle
    shiny_without_puzzle_total += shiny_without_puzzle
    no_rare_fish_after_puzzle_total += no_rare_fish_after_puzzle
    no_rare_fish_without_puzzle_total += no_rare_fish_without_puzzle

# Calculate totals for the entire dataset
after_puzzle_total = shiny_after_puzzle_total + no_rare_fish_after_puzzle_total 
without_puzzle_total = shiny_without_puzzle_total + no_rare_fish_without_puzzle_total
shiny_total = shiny_after_puzzle_total + shiny_without_puzzle_total
no_shiny_total = no_rare_fish_after_puzzle_total + no_rare_fish_without_puzzle_total
total_total = after_puzzle_total + without_puzzle_total

# Print the contingency table for all logs
print("\nContingency Table for All Logs:")
print(f'                       |{"Shiny":^10}|{"No Shiny":^10}|{"Total":^10}')
print(f'-----------------------|----------|----------|----------')
print(f'    After puzzle       |{shiny_after_puzzle_total:^10}|{no_rare_fish_after_puzzle_total:^10}|{after_puzzle_total:^10}')
print(f'    Without puzzle     |{shiny_without_puzzle_total:^10}|{no_rare_fish_without_puzzle_total:^10}|{without_puzzle_total:^10}')
print(f'    Total              |{shiny_total:^10}|{no_shiny_total:^10}|{total_total:^10}')

print(f'opened logs: {opened_logs} \n')

# *** QUI-QUADRADO - X² ***
import numpy as np
from scipy.stats import chi2_contingency
# Dados da tabela de contingência
observed_data = np.array([[shiny_after_puzzle_total, no_rare_fish_after_puzzle_total], [shiny_without_puzzle_total, no_rare_fish_without_puzzle_total]])

# Realiza o teste qui-quadrado
chi2, p, _, _ = chi2_contingency(observed_data)

# Exibe os resultados
print(f"Chi-squared statistic: {chi2}")
print(f"P-value: {p} \n")

# Compara o p-value com um nível de significância (por exemplo, 0.05)
alpha = 0.05
if p < alpha:
    print("Há evidências suficientes para rejeitar a hipótese nula.")
    print("O evento não ocorre ao acaso.")
else:
    print("Não há evidências suficientes para rejeitar a hipótese nula.") 
    print("O evento ocorre ao acaso.")


# *** PROBABILIDADES ***
# Probabilidade de "Shiny after puzzle" (porcentagem)
probability_shiny_after_puzzle = shiny_after_puzzle_total / after_puzzle_total * 100

# Probabilidade de "Shiny sem resolver o puzzle" (porcentagem)
probability_shiny_without_puzzle = shiny_without_puzzle_total / without_puzzle_total * 100

print(f"A probabilidade de um Pokémon ser 'shiny' após resolver um quebra-cabeça é: {probability_shiny_after_puzzle:.4f}%")
print(f"A probabilidade de um Pokémon ser 'shiny' sem resolver um quebra-cabeça é: {probability_shiny_without_puzzle:.4f}%")