
import argparse
from core.pesca_a_dor import main_pesca_a_dor
from core.money_maker import main_money_maker

def main():
    parser = argparse.ArgumentParser(description="pesca-a-dor: fishing bot for PokeXGames")
    parser.add_argument('-m', '--mode', type=int, choices=[1, 2], required=True, help='Select mode: 1 for pesca-a-dor, 2 for money-maker')
    args = parser.parse_args()
    
    if args.mode == 1:
        main_pesca_a_dor()
    elif args.mode == 2:
        main_money_maker()

if __name__ == '__main__':
    main()