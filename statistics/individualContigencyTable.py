import os

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

    after_puzzle_total = shiny_after_puzzle + no_rare_fish_after_puzzle 
    without_puzzle_total = shiny_without_puzzle + no_rare_fish_without_puzzle
    shiny_total = shiny_after_puzzle + shiny_without_puzzle
    no_shiny_total = no_rare_fish_after_puzzle + no_rare_fish_without_puzzle
    total_total = after_puzzle_total + without_puzzle_total

    # Print the contingency table for each log file
    print(f"\nContingency Table for {log_file}:")
    print(f'                       |{"Shiny":^10}|{"No Shiny":^10}|{"Total":^10}')
    print(f'-----------------------|----------|----------|----------')
    print(f'    After puzzle       |{shiny_after_puzzle:^10}|{no_rare_fish_after_puzzle:^10}|{after_puzzle_total:^10}')
    print(f'    Without puzzle     |{shiny_without_puzzle:^10}|{no_rare_fish_without_puzzle:^10}|{without_puzzle_total:^10}')
    print(f'    Total              |{shiny_total:^10}|{no_shiny_total:^10}|{total_total:^10}')

## QUI-QUADRADO - X²

import numpy as np
from scipy.stats import chi2_contingency
# Dados da tabela de contingência
observed_data = np.array([[shiny_after_puzzle, no_rare_fish_after_puzzle], [shiny_without_puzzle, no_rare_fish_without_puzzle]])

# Realiza o teste qui-quadrado
chi2, p, _, _ = chi2_contingency(observed_data)

# Exibe os resultados
print(f"Chi-squared statistic: {chi2}")
print(f"P-value: {p}")

# Compara o p-value com um nível de significância (por exemplo, 0.05)
alpha = 0.05
if p < alpha:
    print("Há evidências suficientes para rejeitar a hipótese nula. \n O evento não ocorre ao acaso.")
else:
    print("Não há evidências suficientes para rejeitar a hipótese nula. \n O evento ocorre ao acaso.")

print(f'opened logs: {opened_logs}')