def sort_key(explosive):
    section_len = len(explosive) // 3
    comp = (
        set(explosive[:section_len])
        .intersection(set(explosive[section_len:2 * section_len]))
        .intersection(set(explosive[2 * section_len:]))
    ).pop()
    return (ord(comp) - ord('a')) if comp.lower() == comp else (100 + ord(comp) - ord('A'))


def sort_explosives(explosives):
    return sorted(explosives, key=sort_key, reverse=True)


if __name__ == "__main__":
    explosives = ["TcYyUQYsWlhheOWBJEhfWNqArqFmAv",
                  "fRLaGGRrMKeVmPiafZTZzqohaWkOAogOp",
                  "bZodJlhbelRJRBBnqLSyslIM",
                  "hHSnMfmPrQfiKcEVCJbhFEutZdaYhglRX",
                  "RdgqxdyFKuoVyVEKlOPgjCfXJaJWUXItJg",
                  "MrcomXDosXHGLDDJaiqkI",
                  "CNKidJwUVESabqQcPYvSYZOjeXteeLStN",
                  "gITpmfSvepyPmgBHsRqmb",
                  "ScFAHyxTkupicstfOboiEtZhgNWqUNcRq",
                  "rPEgfzbrKhiCQZeQEltfGuWENpdpYH"]
    s = sort_explosives(explosives)
    for e in s:
        print(e)