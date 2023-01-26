#!/usr/local/bin/python3
import sys
import signal
import random

# COLORS
RED = "\33[31m"
GREEN = "\33[32m"
YELLOW = "\33[33m"
BLUE = "\33[34m"
BOLD = "\33[1m"
END = "\33[0m"

deck = {}


def signal_handler(sig, frame):
    print()
    sys.exit(0)


def import_deck(file):
    try:
        f = open(file, "r")
    except Exception as e:
        print(f"error: cannot open file {e}")
    with f:
        line = f.readline()
        while line:
            term, definition = line.split("\t")
            deck[term.strip()] = definition.strip()
            line = f.readline()

    f.close()


def add(d, t):
    if t in d:
        d[t] += 1
    else:
        d[t] = 1


def test_terms(terms, missed):
    num_wrong = 0
    total = 0
    wrong = []
    count = 0
    for i in range(len(terms)):
        term = terms[i]
        ans = input(BOLD + f"{term}: " + END)
        total += 1
        # incorrect
        if ans.lower() != deck[term].lower():
            print(BOLD + RED + "incorrect, answer is " + GREEN + deck[term] + END)
            mistake = input(BOLD + YELLOW + "accept as correct? (yes/no) " + END)
            if mistake != "yes":
                add(missed, term)
                num_wrong += 1
                wrong.append(term)
                # type correct answer
                while ans.lower() != deck[term].lower():
                    ans = input(BOLD + BLUE + f"{term}: " + END)
        count += 1
        if count % 20 == 0:
            print(f"=== progress {count}/{len(terms)} terms ===")

    return num_wrong, total, wrong


def run_learn():
    rounds = input("How many times do you want to review each term? ")

    if rounds:
        rounds = int(rounds)
    else:
        rounds = 2

    missed = {}
    num_wrong = 0
    total = 0
    terms = list(deck.keys())
    random.shuffle(terms)

    print(GREEN + f"=== Start Learn {len(terms)} ===" + END)

    # round 1
    print(f"=== round 1 ===")
    w, t, wrong = test_terms(terms, missed)
    num_wrong += w
    total += t
    print(RED + f"{w} incorrect" + END)

    # extra
    i = 0
    for i in range(1, rounds):
        print(f"=== round {i+1} ===")
        terms2 = terms.copy()
        terms2.extend(wrong)
        random.shuffle(terms2)

        w, t, wrong = test_terms(terms2, missed)
        num_wrong += w
        total += t
        print(RED + f"{w} incorrect" + END)

    # remaining incorrects
    while wrong:
        i += 1
        print(f"=== round {i+1} ===")
        random.shuffle(wrong)

        w, t, wrong = test_terms(wrong, missed)
        num_wrong += w
        total += t
        print(RED + f"{w} incorrect" + END)

    print("=== End Learn ===\n")
    print(GREEN + f"SCORE: {total - num_wrong}/{total}\n" + END)
    print(f"=== Missed Terms {len(missed)} ===")
    ordered_missed = sorted(missed.items(), key=lambda x: x[1], reverse=True)
    for term, value in ordered_missed:
        print(f"{term}\t{deck[term]}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"error: must provide at least one deck")
        exit(1)
    signal.signal(signal.SIGINT, signal_handler)
    for i in range(1, len(sys.argv)):
        import_deck(sys.argv[i])

    try:
        run_learn()
    except EOFError as e:
        print()
        sys.exit(0)


# TODO:
# saved state????
