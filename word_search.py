def search_words_in_file(file_path, words):
    """
    Wyszukuje podane słowa w pliku i zwraca wyniki.
    
    Args:
        file_path (str): Ścieżka do pliku
        words (list): Lista słów do wyszukania
    
    Returns:
        dict: Słownik z wynikami wyszukiwania
    """
    results = {}
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        for word in words:
            results[word] = []
            for line_num, line in enumerate(lines, 1):
                if word.lower() in line.lower():
                    results[word].append({
                        'line_number': line_num,
                        'line_content': line.strip()
                    })
        
        return results
    
    except FileNotFoundError:
        print(f"Błąd: Plik '{file_path}' nie został znaleziony.")
        return None
    except Exception as e:
        print(f"Błąd: {e}")
        return None


def main():
    # Przykład użycia
    file_path = "test.txt"
    words_to_search = ["python", "funkcja", "plik"]
    
    results = search_words_in_file(file_path, words_to_search)
    
    if results:
        for word, occurrences in results.items():
            print(f"\nSłowo: '{word}' - znalezione {len(occurrences)} razy:")
            for item in occurrences:
                print(f"  Linia {item['line_number']}: {item['line_content']}")


if __name__ == "__main__":
    main()


#zmienilem wsumie to nic