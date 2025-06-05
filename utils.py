import json
def combine_translations(lang1_file, lang2_file, output_file):
    """
    Combine two translation text files into a JSON file.
    
    Args:
        lang1_file (str): Path to the first language translation file.
        lang2_file (str): Path to the second language translation file.
        output_file (str): Path to save the combined translation file.
    """
    try:
        # Read the first language file
        with open(lang1_file, 'r', encoding='utf-8') as f:
            lang1_lines = [line.strip() for line in f.readlines() if line.strip()]
        
        # Read the second language file
        with open(lang2_file, 'r', encoding='utf-8') as f:
            lang2_lines = [line.strip() for line in f.readlines() if line.strip()]
        
        # Check if both files have the same number of lines
        if len(lang1_lines) != len(lang2_lines):
            print(f"Warning: File '{lang1_file}' has {len(lang1_lines)} lines, "
                  f"file '{lang2_file}' has {len(lang2_lines)} lines. ")
            min_lines = min(len(lang1_lines), len(lang2_lines))
            lang1_lines = lang1_lines[:min_lines]
            lang2_lines = lang2_lines[:min_lines]
            print(f"Using the first {min_lines} lines from both files.")
        
        # Create translation pairs
        translations = []
        for i, (lang1, lang2) in enumerate(zip(lang1_lines, lang2_lines)):
            translations.append({
                "id": i + 1,
                "lang1": lang1,
                "lang2": lang2
            })

        # Write to the output JSON file
        with open(output_file, 'a', encoding='utf-8') as f:
            for i, (lang1, lang2) in enumerate(zip(lang1_lines, lang2_lines)):
                translation_obj = {
                    "id": i + 1,
                    "lang1": lang1,
                    "lang2": lang2
                }
                f.write(json.dumps(translation_obj, ensure_ascii=False) + '\n')
        print(f"Successfully created {output_file} with {len(translations)} translations.")

    except FileNotFoundError as e:
        return FileNotFoundError(e)
    except Exception as e:
        return Exception(f"An error occurred: {e}")