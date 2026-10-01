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

def gc_line_count(line: str) -> float:
    if not line:
        return 0.0
    count = line.count('C') + line.count('G')
    return round(((count / len(line)) * 100), 6)

def gc_content(fasta: dict[str, str]) -> tuple[str, float]:
    if len(fasta) > 10:
        raise ValueError("At most 10 strings")
    for _, value in fasta.items():
        if len(value) > 1000:
            raise ValueError("At most 1kpb each sequence")
    
    gc_dict: dict[str, float] = {}
    for key, value in fasta.items():
        gc_dict[key] = gc_line_count(value)

    max_id = max(gc_dict, key=gc_dict.get)
    max_percent = gc_dict.get(max_id)
    
    return (max_id, max_percent)


if __name__ == "__main__":
    try:
        result_parse: dict[str, str] = parse_fasta("rosalind_gc.txt")
        result_count: tuple[str, float] = gc_content(result_parse)
        max_id, max_percent = result_count
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(max_id)
        print(max_percent)
