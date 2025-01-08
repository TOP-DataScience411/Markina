import shutil
def important_message(text: str) -> str:
    terminal_width = shutil.get_terminal_size().columns - 1
    border = '=' * terminal_width
    text_width = terminal_width - 4
    if current_line:
        lines.append(current_line.strip())
    centered_lines = [line.center(text_width) for line in lines]
    result = []
    result.append(f"# {border} #")
    result.append(f"# {' ' * (terminal_width - 2)} #")
    for line in centered_lines:
        result.append(f"#  {line}  #")
    
    result.append(f"# {' ' * (terminal_width - 2)} #")
    result.append(f"# {border} #")
    
    return "\n".join(result)