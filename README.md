# TTRPG-Initiative-Tracker

> Command Line Utility for tracking a character's initiatives (player turn order) in an encounter in D&D 5e.

To run this utility, you need to install Python3 on your computer:

\*Windows: You can get the installer here - https://www.python.org/downloads/

\*Linux- Ubuntu : `sudo apt install python3.12`

---

From the folder in which you have the initTracker.py file, run:
`python initTracker.py`

There is also a test/demo mode that has a prepopulated list of characters:
`python initTracker.py test`

---

To import a party, place a .json file in the PartyLists that contains the party names, initiatives, dex modifiers, and tie override value (lower goes first). Do not include spaces.
ex. `[
  {
    "name": "Lankas",
    "init": 10,
    "dex": 2,
    "override": 0
  },
  {
    "name": "Imryll",
    "init": 10,
    "dex": 2,
    "override": 0
  }
]`
