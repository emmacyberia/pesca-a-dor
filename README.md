<img align="left" width="70" height="70" src="https://github.com/emmacyberia/pesca-a-dor/blob/main/ui/assets/images/fishing_rod.ico" alt="pesca-a-dor">

# pesca-a-dor

fishing bot for [PokeXGames](https://www.pokexgames.com/). 

Features include: `auto fishing`, `cast spells on shiny Pokémon`, `capture shiny Pokémon`, `collect loot`, and `solve minigame` that appears on the screen every ~5 minutes, allowing uninterrupted fishing.

![](https://github.com/emmacyberia/pesca-a-dor/blob/main/docs/images/pesca-a-dor.gif)

## Minigame

![](https://github.com/emmacyberia/pesca-a-dor/blob/main/docs/images/desafio_de_pesca.gif)

## Usage

### Prerequisites

>[!NOTE]
>Ensure that you have [Conda](https://www.anaconda.com/download/) installed on your system.

```bash
# clone this repository
git clone https://github.com/emmacyberia/pesca-a-dor.git

cd pesca-a-dor

# create a conda environment and install dependencies
conda env create -f environment.yml

# activate the environment
conda activate pesca-a-dor
```

>[!NOTE]
>Before running, ensure that the configuration file is set up properly.
>
>Edit the [configuration file](https://github.com/emmacyberia/pesca-a-dor/blob/main/pesca_a_dor/core/config.py) to match your desired settings.

### Run pesca-a-dor

```bash
# run pesca-a-dor mode
python pesca-a-dor/main.py --mode 1

# run money-maker mode
python pesca-a-dor/main.py --mode 2
```

>[!NOTE]
>Execute [locateOnScreen.py](https://github.com/emmacyberia/pesca-a-dor/blob/main/utils/locateOnScreen.py) to capture coordinates. Hover your mouse over desired locations while the script runs, like pokéball position for `REGION_POKEBALL`.

After adding coordinates to [config.py](https://github.com/emmacyberia/pesca-a-dor/blob/main/pesca_a_dor/core/config.py), run [main.py](https://github.com/emmacyberia/pesca-a-dor/blob/main/pesca_a_dor/main.py) and press `PAGE UP` to start fishing.

## Ingame hotkeys

```
Start fishing           = NumLock
Use food on pokémon     = Caps
Use medicine on pokémon = Backspace
Stand still             = Tab
Collect loot            = CTRL+F5
Use revive              = F1
Order pokémon           = F2
Net Ball                = F10
Janguru Ball            = F11
Tale Ball               = F12
```

## Extra

Pesca-a-dor optimizes performance [multithreading](https://docs.python.org/3.10/library/threading.html#).

## Modes

- [pesca-a-dor](https://github.com/emmacyberia/pesca-a-dor/blob/main/pesca_a_dor/core/pesca_a_dor.py): For Shiny Krabby/Tentacool/Tentacruel/Gyarados project. Generates [logs](https://github.com/emmacyberia/pesca-a-dor/blob/main/pesca_a_dor/logs) for events.
>Can also be used with a weaker Pokémon for your maker to fish, such as a Shedinja (level 60+).
- [money-maker](https://github.com/emmacyberia/pesca-a-dor/blob/main/pesca_a_dor/core/money_maker.py): For Shiny Giant Magikarp project and farm Shiny Magikarp fins (a very lucrative source of income).

## Statistical analysis of shiny occurrences after puzzle resolution

>[!NOTE]
> This game claims that you have a higher chance of fishing shinies after solving the puzzle.
>
> I decided to test this hypothesis and quantify the probability of shiny occurrences after puzzles.
>
> **Spoiler: Indeed, the shiny rate is higher xD**
>
> The null hypothesis for the [chi-square test](https://en.wikipedia.org/wiki/Chi-squared_test) posits that there is no significant association between the variables being examined, while the alternative hypothesis asserts the presence of a significant relationship.
>
> The chi-square test was employed to assess whether the observed data significantly deviate from what would be expected under the assumption of independence between the variables, providing insights into the association between puzzle resolution and the occurrence of shiny Pokémon.
>
> In this case, the formulated hypotheses are:
>
> H0: `**There is no association**` between puzzle resolution and the occurrence of shiny Pokémon
>
> H1: `**There is an association**` between puzzle resolution and the occurrence of shiny Pokémon
>
> Significance level = 0.05

### Contingency Tables

<details>
  <summary>Krabby ~70+ logs (days), more than 500 hours collected</summary>

  |         |  Shiny   | No Shiny |  Total
  |---------|----------|----------|----------
  | After   |   504    |   8541   |   9045
  | Without |   1367   |  85423   |  86790
  | Total   |   1871   |  93964   |  95835
</details>

<details>
  <summary>Tentacool ~70+ logs (days), more than 500 hours collected</summary>

  |         |  Shiny   | No Shiny |  Total
  |---------|----------|----------|----------
  | After   |    48    |   8541   |   8589
  | Without |   246    |  85423   |  85669
  | Total   |   294    |  93964   |  94258
</details>

### Chi-squared Test Results

<details>
  <summary>Krabby</summary>

  - Chi-squared statistic: 681.5909869816392
  
  - P-value: 3.0125967571505313e-150
</details>

>[!NOTE]
>There is enough evidence to reject the null hypothesis for Krabby.
>
>The occurrence of shiny Krabby is not random.
>
>In other words, solving the puzzle is associated with an **increased rate** of shiny Krabby.

<details>
  <summary>Tentacool</summary>
  
  - Chi-squared statistic: 17.670234869403
  - P-value: 2.6270550990164333e-05
</details>

>[!NOTE]
>The occurrence of shiny Tentacool is not random.
>
>In other words, solving the puzzle is associated with an **increased rate** of shiny Tentacool.

## Probability Analysis

![](https://github.com/emmacyberia/pesca-a-dor/blob/main/docs/images/ShinyKrabby.gif)
- Probability to fish a shiny Krabby after solving a puzzle: `5.5721%`
- Probability to fish a shiny Krabby without a puzzle: `1.5751%`

![](https://github.com/emmacyberia/pesca-a-dor/blob/main/docs/images/ShinyTentacool.gif)
- Probability to fish a shiny Tentacool after solving a puzzle: `0.5589%`
- Probability to fish a shiny Tentacool without a puzzle: `0.2872%`

## Achievements

```
27/04/2023 - 1st night 100% AFK
04:08 You caught a Pokémon! (Krabby).
04:08 You've wasted: 144 Ultra Balls and 407 Net Balls to catch it.
```

```
23:26 You caught a Pokémon! (Krabby).
23:26 You've wasted: 200 Net Balls to catch it.
```

```
05:47 You caught a Pokémon! (Krabby).
05:47 You've wasted: 20 Net Balls to catch it.
```

```
00:06 You caught a Pokémon! (Krabby).
00:06 You've wasted: 499 Net Balls to catch it.
```
