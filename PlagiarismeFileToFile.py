import re

def cek_perbedaan_kode(file1, file2):
    try:
        kode1 = read_file(file1)
        kode2 = read_file(file2)

        overall_similarity = compare_files(kode1, kode2)

        features1 = extract_features(kode1)
        features2 = extract_features(kode2)

        data_types_similarity = calculate_similarity(features1['data_types'], features2['data_types'])
        variables_similarity = calculate_similarity(features1['variables'], features2['variables'])
        arithmetic_ops_similarity = calculate_similarity(features1['arithmetic_ops'], features2['arithmetic_ops'])

        overall_similarity = (overall_similarity + data_types_similarity + variables_similarity + arithmetic_ops_similarity) / 4

        return generate_report(overall_similarity)

    except FileNotFoundError:
        return "Salah satu file tidak ditemukan."

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def compare_files(kode1, kode2):
    min_len = min(len(kode1), len(kode2))
    match_count = sum(1 for i in range(min_len) if kode1[i] == kode2[i])

    total_chars = max(len(kode1), len(kode2))
    similarity_percent = (match_count / total_chars) * 100
    return similarity_percent

def extract_features(kode):
    return {
        'data_types': find_data_types(kode),
        'variables': find_variables(kode),
        'arithmetic_ops': find_arithmetic_operations(kode)
    }

def find_data_types(kode):
    types = re.findall(r'\b(int|float|double|String|char|boolean)\b', kode)
    return set(types)

def find_variables(kode):
    variables = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\b', kode)
    reserved_keywords = {'int', 'float', 'double', 'String', 'char', 'boolean'}
    return set(variables) - reserved_keywords

def find_arithmetic_operations(kode):
    operations = re.findall(r'\b(\+|\-|\*|\/|\%)\b', kode)
    return set(operations)

def calculate_similarity(set1, set2):
    intersection = set1.intersection(set2)
    if len(set1) == 0 and len(set2) == 0:
        return 100
    return (len(intersection) / max(len(set1), len(set2))) * 100

def generate_report(overall_similarity):
    return f"Plagiarisme : {overall_similarity:.2f}%"

file1 = 'NamaFile.pwn'
file2 = 'NamaFile.pwn'

hasil = cek_perbedaan_kode(file1, file2)
print(hasil)
