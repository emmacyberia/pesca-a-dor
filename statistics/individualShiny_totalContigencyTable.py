import os

# Initialize counts for all categories for Krabby and Tentacool
shiny_after_puzzle_krabby_total = 0
shiny_without_puzzle_krabby_total = 0
no_rare_fish_after_puzzle_krabby_total = 0
no_rare_fish_without_puzzle_krabby_total = 0

shiny_after_puzzle_tentacool_total = 0
shiny_without_puzzle_tentacool_total = 0
no_rare_fish_after_puzzle_tentacool_total = 0
no_rare_fish_without_puzzle_tentacool_total = 0

# List all files in the 'logs' directory
log_files = os.listdir("logs")
opened_logs = 0

# Process each log file
for log_file in log_files:
    opened_logs += 1
    # Read logs
    with open(os.path.join("logs", log_file), "r", encoding="ISO-8859-1") as file:
        logs = file.readlines()

    shiny_after_puzzle_krabby = 0
    shiny_without_puzzle_krabby = 0
    no_rare_fish_after_puzzle_krabby = 0
    no_rare_fish_without_puzzle_krabby = 0

    shiny_after_puzzle_tentacool = 0
    shiny_without_puzzle_tentacool = 0
    no_rare_fish_after_puzzle_tentacool = 0
    no_rare_fish_without_puzzle_tentacool = 0

    # Logs processing
    for i, line in enumerate(logs):
        if "Wild pokémon appeared!" in line:
            # Check if the previous line [line - 2] contains the message "Solving puzzle..."
            # Also check if the line before [line - 1] contains "..."
            if "..." in logs[i - 1] and "Solving puzzle..." in logs[i - 2]:
                if "Shiny Krabby" in logs[i+1]:
                    shiny_after_puzzle_krabby += 1
                elif "Shiny Tentacool" in logs[i+1]:
                    shiny_after_puzzle_tentacool += 1
            else:
                if "Shiny Krabby" in logs[i+1]:
                    shiny_without_puzzle_krabby += 1
                elif "Shiny Tentacool" in logs[i+1]:
                    shiny_without_puzzle_tentacool += 1
        
        elif "Solving puzzle..." in line:
            # If there is "..." after solving the puzzle, consider it as "No Rare Fish" after the puzzle
            if i + 2 < len(logs) and "..." in logs[i + 2]:
                no_rare_fish_after_puzzle_krabby += 1
                no_rare_fish_after_puzzle_tentacool += 1

        elif "..." in line:
            # If there is "..." and there is no "Solving puzzle..." before, consider it as "No Rare Fish" without puzzle
            if i > 0 and "Solving puzzle..." not in logs[i - 1]:
                no_rare_fish_without_puzzle_krabby += 1
                no_rare_fish_without_puzzle_tentacool += 1

    # Accumulate counts for each category for Krabby and Tentacool
    shiny_after_puzzle_krabby_total += shiny_after_puzzle_krabby
    shiny_without_puzzle_krabby_total += shiny_without_puzzle_krabby
    no_rare_fish_after_puzzle_krabby_total += no_rare_fish_after_puzzle_krabby
    no_rare_fish_without_puzzle_krabby_total += no_rare_fish_without_puzzle_krabby

    shiny_after_puzzle_tentacool_total += shiny_after_puzzle_tentacool
    shiny_without_puzzle_tentacool_total += shiny_without_puzzle_tentacool
    no_rare_fish_after_puzzle_tentacool_total += no_rare_fish_after_puzzle_tentacool
    no_rare_fish_without_puzzle_tentacool_total += no_rare_fish_without_puzzle_tentacool

# Calculate totals for the entire dataset for Krabby
after_puzzle_total_krabby = shiny_after_puzzle_krabby_total + no_rare_fish_after_puzzle_krabby_total 
without_puzzle_total_krabby = shiny_without_puzzle_krabby_total + no_rare_fish_without_puzzle_krabby_total
shiny_total_krabby = shiny_after_puzzle_krabby_total + shiny_without_puzzle_krabby_total
no_shiny_total_krabby = no_rare_fish_after_puzzle_krabby_total + no_rare_fish_without_puzzle_krabby_total

# Calculate totals for the entire dataset for Tentacool
after_puzzle_total_tentacool = shiny_after_puzzle_tentacool_total + no_rare_fish_after_puzzle_tentacool_total 
without_puzzle_total_tentacool = shiny_without_puzzle_tentacool_total + no_rare_fish_without_puzzle_tentacool_total
shiny_total_tentacool = shiny_after_puzzle_tentacool_total + shiny_without_puzzle_tentacool_total
no_shiny_total_tentacool = no_rare_fish_after_puzzle_tentacool_total + no_rare_fish_without_puzzle_tentacool_total

# Print the contingency table for Krabby
print("\nContingency Table for Krabby:")
print(f'                       |{"Shiny":^10}|{"No Shiny":^10}|{"Total":^10}')
print(f'-----------------------|----------|----------|----------')
print(f'    After puzzle       |{shiny_after_puzzle_krabby_total:^10}|{no_rare_fish_after_puzzle_krabby_total:^10}|{after_puzzle_total_krabby:^10}')
print(f'    Without puzzle     |{shiny_without_puzzle_krabby_total:^10}|{no_rare_fish_without_puzzle_krabby_total:^10}|{without_puzzle_total_krabby:^10}')
print(f'    Total              |{shiny_total_krabby:^10}|{no_shiny_total_krabby:^10}|{(after_puzzle_total_krabby + without_puzzle_total_krabby):^10}')

# Print the contingency table for Tentacool
print("\nContingency Table for Tentacool:")
print(f'                       |{"Shiny":^10}|{"No Shiny":^10}|{"Total":^10}')
print(f'-----------------------|----------|----------|----------')
print(f'    After puzzle       |{shiny_after_puzzle_tentacool_total:^10}|{no_rare_fish_after_puzzle_tentacool_total:^10}|{after_puzzle_total_tentacool:^10}')
print(f'    Without puzzle     |{shiny_without_puzzle_tentacool_total:^10}|{no_rare_fish_without_puzzle_tentacool_total:^10}|{without_puzzle_total_tentacool:^10}')
print(f'    Total              |{shiny_total_tentacool:^10}|{no_shiny_total_tentacool:^10}|{(after_puzzle_total_tentacool + without_puzzle_total_tentacool):^10}')

print(f'opened logs: {opened_logs} \n')

# QUI-QUADRADO KRABBY
import numpy as np
from scipy.stats import chi2_contingency

# Dados da tabela de contingência para Krabby
observed_data_krabby = np.array([[shiny_after_puzzle_krabby_total, no_rare_fish_after_puzzle_krabby_total],
                                 [shiny_without_puzzle_krabby_total, no_rare_fish_without_puzzle_krabby_total]])

# Realiza o teste qui-quadrado para Krabby
chi2_krabby, p_krabby, _, _ = chi2_contingency(observed_data_krabby)

# Exibe os resultados para Krabby
print("\nResults for Krabby:")
print(f"Chi-squared statistic: {chi2_krabby}")
print(f"P-value: {p_krabby} \n")

# Compara o p-value com um nível de significância (por exemplo, 0.05)
alpha = 0.05
if p_krabby < alpha:
    print("Há evidências suficientes para rejeitar a hipótese nula para Krabby.")
    print("O evento não ocorre ao acaso para Krabby.")
else:
    print("Não há evidências suficientes para rejeitar a hipótese nula para Krabby.") 
    print("O evento ocorre ao acaso para Krabby.")

# QUI-QUADRADO TENTACOOL
# Dados da tabela de contingência para Tentacool
observed_data_tentacool = np.array([[shiny_after_puzzle_tentacool_total, no_rare_fish_after_puzzle_tentacool_total],
                                    [shiny_without_puzzle_tentacool_total, no_rare_fish_without_puzzle_tentacool_total]])

# Realiza o teste qui-quadrado para Tentacool
chi2_tentacool, p_tentacool, _, _ = chi2_contingency(observed_data_tentacool)

# Exibe os resultados para Tentacool
print("\nResults for Tentacool:")
print(f"Chi-squared statistic: {chi2_tentacool}")
print(f"P-value: {p_tentacool} \n")

# Compara o p-value com um nível de significância (por exemplo, 0.05)
alpha = 0.05
if p_tentacool < alpha:
    print("Há evidências suficientes para rejeitar a hipótese nula para Tentacool.")
    print("O evento não ocorre ao acaso para Tentacool.")
else:
    print("Não há evidências suficientes para rejeitar a hipótese nula para Tentacool.") 
    print("O evento ocorre ao acaso para Tentacool.")

# Probabilidade de "Shiny after puzzle" para Krabby (porcentagem)
probability_shiny_after_puzzle_krabby = shiny_after_puzzle_krabby_total / after_puzzle_total_krabby * 100

# Probabilidade de "Shiny sem resolver o puzzle" para Krabby (porcentagem)
probability_shiny_without_puzzle_krabby = shiny_without_puzzle_krabby_total / without_puzzle_total_krabby * 100

print(f"A probabilidade de um Pokémon Krabby ser 'shiny' após resolver um quebra-cabeça é: {probability_shiny_after_puzzle_krabby:.4f}%")
print(f"A probabilidade de um Pokémon Krabby ser 'shiny' sem resolver um quebra-cabeça é: {probability_shiny_without_puzzle_krabby:.4f}%")

# Probabilidade de "Shiny after puzzle" para Tentacool (porcentagem)
probability_shiny_after_puzzle_tentacool = shiny_after_puzzle_tentacool_total / after_puzzle_total_tentacool * 100

# Probabilidade de "Shiny sem resolver o puzzle" para Tentacool (porcentagem)
probability_shiny_without_puzzle_tentacool = shiny_without_puzzle_tentacool_total / without_puzzle_total_tentacool * 100

print(f"A probabilidade de um Pokémon Tentacool ser 'shiny' após resolver um quebra-cabeça é: {probability_shiny_after_puzzle_tentacool:.4f}%")
print(f"A probabilidade de um Pokémon Tentacool ser 'shiny' sem resolver um quebra-cabeça é: {probability_shiny_without_puzzle_tentacool:.4f}%")