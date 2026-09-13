def print_full_boxed_art():
    art_lines = [
        "░█████╗░███╗░░██╗░█████╗░███╗░░██╗██╗░░██╗███████╗",
        "██╔══██╗████╗░██║██╔══██╗████╗░██║██║░██╔╝██╔════╝",
        "███████║██╔██╗██║██║░░██║██╔██╗██║█████═╝░█████╗░░",
        "██╔══██║██║╚████║██║░░██║██║╚████║██╔═██╗░██╔══╝░░",
        "██║░░██║██║░╚███║╚█████╔╝██║░╚███║██║░╚██╗███████╗",
        "╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝"
    ]
    
    box_width = len(art_lines[0]) + 4
    top_border = "┌" + "─" * (box_width - 2) + "┐"
    bottom_border = "└" + "─" * (box_width - 2) + "┘"
    
    border_color = "\033[38;2;0;140;255m"  # Çerçeve rengi (Mavi)
    reset = "\033[0m"
    
    print(f"{border_color}{top_border}{reset}")
    
    # Yazıyı ve renk geçişini kutunun içine yerleştir
    for line in art_lines:
        colored_line = ""
        for j, char in enumerate(line):
            if char == " ":
                colored_line += " "
                continue
            
            factor = j / max(1, len(line) - 1)
            r = 0
            g = int(100 + 155 * factor)
            b = int(255 - 135 * factor)
            
            colored_line += f"\033[38;2;{r};{g};{b}m{char}"
            
        print(f"{border_color}│ {reset}{colored_line} {border_color}│{reset}")
        
    # Alt bilgi satırı (Sağa dayalı)
    footer = "[⚡] ANONKE"
    padded_footer = footer.rjust(len(art_lines[0]))
    colored_footer = ""
    for j, char in enumerate(padded_footer):
        factor = j / max(1, len(padded_footer) - 1)
        r = 0
        g = int(150 + 105 * factor)
        b = int(200 - 100 * factor)
        colored_footer += f"\033[38;2;{r};{g};{b}m{char}"
        
    print(f"{border_color}│ {reset}{colored_footer} {border_color}│{reset}")
    print(f"{border_color}{bottom_border}{reset}")

if __name__ == "__main__":
    print_full_boxed_art()

