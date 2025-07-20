def security_system(passcode_attempts: list[str]):
    for a in passcode_attempts:
        if a == "ABCD":
            return True
    return False


if __name__ == "__main__":
    attempts = ["AAAAAAA",
                "CDEFGHI",
                "BUGS",
                "ZZZAAA",
                "B",
                "CDEFGHIJK",
                "ABC"]
    print(security_system(attempts))
