def security_system(passcode_attempts: list[str]):
    all_entries = iter("".join(passcode_attempts))
    return all(c in all_entries for c in "ABCD")


if __name__ == "__main__":
    attempts = ["AAAAAAA",
                "CDEFGHI",
                "BUGS",
                "ZZZAAA",
                "B",
                "CDEFGHIJK",
                "ABC"]
    print(security_system(attempts))
