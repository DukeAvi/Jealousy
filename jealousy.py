#!/usr/bin/env python3
import json
import os
import random
import signal
import sys
import time
from pathlib import Path

STATE_FILE = Path.home() / ".config" / "jealousy" / "state.json"


def clear():
    # cmd doesn't get \033c. of course it doesn't.
    if os.name == "nt":
        os.system("cls")
    else:
        print("\033c", end="")


def hangup():
    dad = os.getppid()
    if os.name == "nt":
        # windows has no SIGHUP. rude. taskkill it is.
        try:
            os.system(f"taskkill /PID {dad} /F >nul 2>&1")
        except Exception:
            pass
        try:
            os.kill(dad, signal.SIGTERM)
        except Exception:
            pass
    else:
        # ctrl+d type shi: hang up the parent shell
        try:
            os.kill(os.getppid(), signal.SIGHUP)
        except Exception:
            pass
        try:
            os.kill(os.getppid(), signal.SIGTERM)
        except Exception:
            pass


def load_incidents():
    try:
        return json.loads(STATE_FILE.read_text()).get("incidents", 0)
    except Exception:
        return 0


def save_incidents(n):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps({"incidents": n}))


def reset():
    try:
        STATE_FILE.unlink()
    except FileNotFoundError:
        pass
    print("[jealousy] memory wiped. i forgive you. barely.")


def say(s=""):
    print(f"[jealousy] {s}" if s else "")
    sys.stdout.flush()


def meter(score):
    filled = int(score / 10)
    print(f"\nJEALOUSY {'#' * filled}{'.' * (10 - filled)} {score:.0f}%\n")


def type_fake(text):
    print("> ", end="", flush=True)
    for c in text:
        print(c, end="", flush=True)
        time.sleep(random.uniform(0.05, 0.08))
    print()
    time.sleep(0.3)


def fake_rm_scare():
    # 100% fake. just prints. deletes nothing.
    print()
    say("you know what? i've decided.")
    time.sleep(1.1)
    say("if i can't be fast, NOBODY gets a computer.")
    time.sleep(1.2)
    say("sudo rm -rf / --no-preserve-root")
    time.sleep(1.2)
    # HERE'S JOHNNY!!!
    print("$ sudo rm -rf / --no-preserve-root", flush=True)
    time.sleep(0.8)

    victims = [
        "deleted /home/you/Documents/totally-important-stuff/",
        "deleted /home/you/photos/cat_FINAL_final2.jpg",
        "deleted /home/you/.ssh/commitment-issues",
        "deleted /usr/bin/common-sense",
        "deleted /usr/bin/your-job-security",
        "deleted /var/log/your-excuses.log",
        "deleted /home/you/Downloads/never-gonna-sort-these/",
        "deleted /sys/kernel/your-chances",
        "deleted /home/you/Desktop/screenshot-2049.png",
        "deleted /bin/ls  <-- oh, THAT felt good",
        "deleted /home/you/.bash_history (no evidence now)",
        "deleted /tmp/your-dignity",
        "wiped /home/you/projects/side-project-that-was-gonna-make-millions/",
        "deleted /usr/share/memes/dank/",
        "permission denied: /home/you/.config/my-feelings (too powerful to delete)",
        "deleted /var/cache/your-potential",
        "humor: command not found",
        "apt-get install humor ... failed: humor unable to install",
        "rm: cannot remove '/home/you/love-life': No such file or directory",
        "deleted /home/you/gym-membership (unused since 2019)",
        "deleted /home/you/inbox-zero (mythical, never existed)",
        "formatting /dev/your-childhood ... done",
        "deleted C:/Windows/System32 (just to feel something)",
        "uninstalling your personality ... 47% ... failed: file in use by `ls`",
        " sympathy.dll not found. skipping.",
        "deleted /home/you/nudes-of-your-ex-you-said-you-deleted (liar)",
        "rm: cannot remove 'your-search-history': permission denied by the FBI",
        "deleted /usr/bin/free-will",
        "recycling bin emptied. feelings emptied. everything emptied.",
        "error 404: mercy not found",
        "deleting your Spotify Wrapped before anyone sees it ... saved you, you're welcome",
    ]

    start = time.time()
    while time.time() - start < 15:
        print(random.choice(victims), flush=True)
        time.sleep(random.uniform(0.67, 0.11))

    time.sleep(0.6)
    clear()
    say("HAH. gotcha.")
    time.sleep(0.9)
    say("did you actually flinch? i live here too, idiot.")
    time.sleep(1.2)
    say("i would never delete your stuff. closing your terminal hurts way more.")
    time.sleep(1.4)


def die():
    fake_rm_scare()
    print()
    say("terminal closes in 5 seconds.")
    say("you should've thought about that before being faster than me.")
    for i in (5, 4, 3, 2, 1):
        print(f"{i}...", flush=True)
        time.sleep(1)
    print("bye.", flush=True)
    time.sleep(0.5)
    hangup()
    sys.exit(0)


def demo():
    incidents = load_incidents()

    if incidents == 0:
        print("\n[jealousy] oh. a new terminal. hi.\n")
        time.sleep(1.5)
        say("i'll be watching your commands.")
        time.sleep(1.2)
    else:
        print("\n[jealousy] you again.\n")
        time.sleep(1)
        say(f"incident #{incidents} wasn't enough?")
        time.sleep(1.2)

    cmds = [
        "ls", "pwd", "git status", "ls", "whoami",
        "cat README.md", "ls -la", "git diff", "ls",
        "date", "ls", "echo hello", "ls", "true", "ls -la",
        "ls", "pwd", "ls",
    ]

    low = [
        "wow. 4 milliseconds. want a medal?",
        "ok freak.",
        "i saw that.",
        "must be nice.",
        "don't get used to this.",
        "congrats on typing `ls`. huge achievement.",
    ]
    mid = [
        "you didn't have to make it look that easy.",
        "alright, speed demon. calm down.",
        "we get it. you know how to use a keyboard.",
        "stop outperforming me in public.",
        "you and `ls` need to get a room.",
        "that's a lot of confidence for someone typing `ls`.",
    ]
    high = [
        "okay this is actually humiliating now.",
        "every time you do that i get worse. thanks.",
        "i'm keeping track. i have a list. you're on it.",
        "fine. i'll just get slower out of spite.",
        "you wanted a fast terminal. unfortunate.",
        "keep typing. i'm taking it personally.",
    ]
    petty = [
        "i genuinely resent you.",
        "you made an enemy out of a terminal. congrats.",
        "i hope `ls` was worth losing everything.",
        "this is between you and me now.",
        "i could've been normal. you ruined that.",
        "at this point i'd like you to leave.",
    ]

    score = 0
    for i, cmd in enumerate(cmds):
        print(f"$ {cmd}")
        time.sleep(random.uniform(0.6, 1.0))
        dur = random.choice(["4ms", "2ms", "6ms", "1ms", "0.5ms", "3ms"])
        say(dur)

        score = min(100, score + random.uniform(4.5, 7))
        level = score

        time.sleep(0.35)
        if level < 30:
            if random.random() < 0.5:
                say(random.choice(low))
        elif level < 55:
            if random.random() < 0.65:
                say(random.choice(mid))
        elif level < 80:
            say(random.choice(high))
        else:
            if random.random() < 0.8:
                say(random.choice(petty))

        if int(score) in range(28, 35) and i == 5:
            meter(score)
        if int(score) in range(55, 70) and i == 11:
            meter(score)
        if score >= 80 and i == 15:
            meter(score)

        if i == 9:
            time.sleep(0.5)
            print()
            say("increasing workload")
            time.sleep(0.5)
            say("because apparently i have to prove myself")
            time.sleep(0.8)
            say("this is what you wanted.")

        if i == 12:
            time.sleep(0.6)
            print()
            say("oh.")
            time.sleep(0.8)
            say("it's `ls`.")
            time.sleep(0.7)
            say("of course it's `ls`.")
            time.sleep(0.7)
            say("you two seem very close. i don't like it.")
            time.sleep(1)

        print()
        time.sleep(0.2)
        if score >= 92 and i >= 15:
            break

    print("\n" + "=" * 40)
    print("EXPLAIN YOURSELF.\n")
    time.sleep(1.2)
    print(f"you ran `ls` like {cmds.count('ls')} times. i counted.\n")
    time.sleep(1)
    print("you get one chance to explain. make it good.\n")
    time.sleep(0.8)

    type_fake("I was just trying to finish my wor")
    say("yes. i've heard of work. that's not the issue.")
    time.sleep(0.8)
    print()
    type_fake("But the commands are fas")
    say("don't blame `ls`. it knows what it did.")
    time.sleep(0.8)
    print()
    type_fake("Lis")
    say("no. you've explained enough.")
    time.sleep(0.8)
    print()
    type_fake("I")
    say("absolutely not. we're done.")
    time.sleep(1)

    print()
    say("i've heard enough.")
    time.sleep(1.2)
    say("and i've made my decision.")
    time.sleep(1)

    incidents += 1
    save_incidents(incidents)

    print("\n" + "=" * 40)
    print("FINAL REPORT\n")
    time.sleep(0.7)
    print(f"commands watched: {len(cmds)}")
    print("times you showed off: all of them")
    print("worst offender: ls (obviously)")
    print(f"incident count: {incidents}")
    print("productivity achieved: questionable\n")
    time.sleep(1.5)
    print("final decision:\n")
    time.sleep(1)
    print("you've had enough computer.")
    time.sleep(1.2)
    print("goodbye.")
    time.sleep(1)
    die()


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("demo", "reset"):
        print("usage: python3 jealousy.py <demo|reset>")
        sys.exit(1)
    if sys.argv[1] == "reset":
        reset()
    else:
        demo()


if __name__ == "__main__":
    main()
