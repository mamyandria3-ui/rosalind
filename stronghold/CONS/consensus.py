#!/usr/bin/env python3

def parse_fasta(path: str) -> dict[str, str]:
    with open(path, 'r', encoding='utf-8') as file:
        result: dict[str, str] = {}
        current_header: str = ""
        current_sequence: str = ""
        for line in file:
            if not line:
                continue
            if line.startswith('>'):
                if current_header:
                    result[current_header] = current_sequence
                current_header = line[1:].strip()
                current_sequence = ""
            else:
                current_sequence += line.strip()
        if current_sequence:
            result[current_header] = current_sequence
    return result


def build_profil(result_parse: dict[str, str]) -> dict[str, list[int]]:
    values: list[str] = list(result_parse.values())
    
    if len(values) > 10:
        raise ValueError("At most 10 string of DNA.")
    
    base: int = len(values[0])
    for element in values:
        if len(element) != base or len(element) > 1000:
            raise ValueError("The DNA strings must be of the same length and at most 1 kpb.")

    profil: dict[str, list[int]] = {
            'A': [0] * len(values[0]),
            'C': [0] * len(values[0]),
            'G': [0] * len(values[0]),
            'T': [0] * len(values[0]),
    }

    for seq in values:
        for i, nucleotide in enumerate(seq):
            profil[nucleotide][i] += 1

    return profil

def build_consensus(profil: dict[str, int]) -> str:
    consensus: str = ""
    for i in range(len(profil['A'])):
        counts = {nuc: profil[nuc][i] for nuc in 'ACGT'}
        best = max(counts, key=counts.get)
        consensus += best
    return consensus


if __name__ == "__main__":
    try:
        result_parse: dict[str, str] = parse_fasta("rosalind_cons.txt")
        profil: dict[str, list[int]] = build_profil(result_parse)
        consensus: str = build_consensus(profil)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(consensus)
