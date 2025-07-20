import string


def monologue_analyzer(monologue):
    words = [word.lower().strip(string.punctuation) for word in monologue.split(" ")]
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1

    top_counts = sorted(list(counts.items()), key=lambda x: counts[x[0]], reverse=True)
    for i in range(3):
        print(f"{top_counts[i][0]}: {top_counts[i][1]}")


if __name__ == "__main__":
    monologue = """Well, well, Spy Thon, it seems your meddling days are over. You see, while you were busy playing the hero, I've been perfecting my ultimate creation - the Bugotron 9000! Yes, this magnificent machine harnesses the power of bugs! With just a flick of a switch, it will unleash bugs to disrupt even the most secure system. An unstoppable wave of my bugs will be unleashed upon the world! Every line of code will fail, every firewall will crumble! And you, my dear Spy Thon, are powerless to stop it! You thought you could outsmart me, but no! Even you, the great Spy Thon, has fallen victim to my bugs! Your security disabled and your beacons scrambled by my beautiful bugs! And if the Spy Thon cannot defeat the bugs, who can? Ha ha ha!"""
    monologue_analyzer(monologue)
