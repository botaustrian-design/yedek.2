def print_custom_art():
    # Gönderdiğin özel pikselli ANONKE tasarımı
    art_lines = [
        "░█████╗░███╗░░██╗░█████╗░███╗░░██╗██╗░░██╗███████╗",
        "██╔══██╗████╗░██║██╔══██╗████╗░██║██║░██╔╝██╔════╝",
        "███████║██╔██╗██║██║░░██║██╔██╗██║█████═╝░█████╗░░",
        "██╔══██║██║╚████║██║░░██║██║╚████║██╔═██╗░██╔══╝░░",
        "██║░░██║██║░╚███║╚█████╔╝██║░╚███║██║░╚██╗███████╗",
        "╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝"
    ]
    
    max_len = max(len(l) for l in art_lines)
    
    for line in art_lines:
        colored_line = ""
        for j, char in enumerate(line):
            if char == " ":
                colored_line += " "
                continue
            
            # Yatay eksende sol (mavi) sağ (yeşil) renk geçişi
            factor = j / max(1, max_len - 1)
            r = 0
            g = int(100 + 155 * factor)
            b = int(255 - 135 * factor)
            
            colored_line += f"\033[38;2;{r};{g};{b}m{char}"
            
        print(colored_line + "\033[0m")

if __name__ == "__main__":
    print_custom_art()

